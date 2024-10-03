import numpy as np
import math
from OCC.Core.gp import gp_Pnt, gp_Ax2
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.TopoDS import TopoDS_Shape

import classes.mesh.helper as helper
from classes.logger import log

from classes.app import get_app


TIP_LENGTH = 2.5


class NeedleChannel:

    @staticmethod
    def default_diameter() -> float: return get_app().values.config_values.get("CONFIG_CHANNELS_DIAMETER")

    def get_diameter(self):
        return self._diameter
    
    def set_diameter(self, diameter: float) -> None:
        self._diameter = diameter
        self._shape = None
        self.shape()

    def set_offset(self, height: float = 0.0) -> None:
        self._offset = height
        self._shape = None
        self.shape()

    ''' #getOffset() function is not currently in use.  It is left here in case it is needed in the future.
    def getOffset(self) -> float:
        return self._offset
    '''
    
    def get_points(self) -> list:
        return [ [
            point[0], 
            point[1], 
            point[2] + self._offset
            ] for point in self.points]

    # ref:
    # https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python/13849249#13849249
    # https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-vectors
    def get_rotation(self):
        # calculate the sin angle on the xy plane using 0,0 and the highest point in the list of points
        v1 = [1.0, 0.0, self.points[0][2]]
        v2 = self.points[0]
        angle = math.atan2(v2[1] - v1[1], v2[0] - v1[0]) * \
            (180 / 3.14159)  # convert to degrees
        log.debug(f"needle channel angle: {self.points[0]} : {angle}")

        # ensuring the angle stays between 0 and 360 degrees
        while angle < 0:
            angle += 360
            log.debug(f"Small Angle! corrected to {angle}")

        while angle > 360:
            angle -= 360
            log.debug(f"Large angle! corrected to {angle}")

        return angle

    def shape(self) -> TopoDS_Shape:
        if self._shape:
            return self._shape

        self._shape = rounded_channel(self.points, self._offset, self._diameter)
        
        return self._shape
    
    def __init__(self, roi_number: str, channel_number: str, label: str, points):
        self.roi_number = roi_number
        self.channel_number = channel_number
        self.label = label
        self.points = points
        self.points_raw = points
        self._shape = None

        self._offset = 0.0
        self._diameter = get_app().values.config_values.get("CONFIG_CHANNELS_DIAMETER")

def rounded_channel(channel_points, offset: float = 0.0, diameter: float = 3.0) -> TopoDS_Shape:
    """
    If a needle channel has a long distance between the first and second point, this helps stub it
    """
    # offset points using z axis and cylinder's offset
    # and convert into a gp_Pnt
    # rounding/truncation is needed otherwise there can be a bug in pipe = BRepAlgoAPI_Fuse(cone, pipe).Shape() below.
    window = get_app().window
    channel_points = np.array(channel_points)
    
    # apply the offset for the cylinder length
    # all rows column 3
    channel_points[:,2] += offset

    # Number of decimal places to keep
    decimals = 5

    # Truncate without rounding
    channel_points = np.floor(channel_points * 10**decimals) / 10**decimals

    channel_points = remove_identical_points(channel_points)

    channel_points = remove_collinear_points(channel_points) 
    
    points = [gp_Pnt(point[0], point[1], point[2]) for point in channel_points]

    radius = diameter/2

    # generate starting point on top (cone)
    p1 = points[0]
    p2 = points[1]
    check = [0,1]

    try:
        check = create_point(p1, p2, radius)
    except:
        pass
    if(check[1]):
        log.warning("warning thrown while constructing needle tips")
    pipe = check[0]

    def fix1(): #returns -1 if error, 0 if warning, 1 if success
        # tries increasing the radius by an infinitesimal amount (0.001), then fusing.
        try:
            cylinder = pipe_segment(p1, p2, radius+0.001)
            tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder)
            if tempfuse.HasWarnings():
                return [0,tempfuse]
            return [1, tempfuse]
        except:
            return [-1, tempfuse]
        
    def fix2(): # tries rounding to different amounts of decimals, then fusing.
        max_attempt_value = -1#-1 if error, 0 if warning, 1 if success
        for i in [4,3,2]:
            #may introduce some rounding error (up to 0.01 can correct later if need be)
            p1.SetX(round(p1.X(),i))
            p1.SetY(round(p1.Y(),i))
            p1.SetZ(round(p1.Z(),i))
            p2.SetX(round(p2.X(),i))
            p2.SetY(round(p2.Y(),i))
            p2.SetZ(round(p2.Z(),i))
            cylinder = pipe_segment(p1, p2, radius+0.001)
            try:
                tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder)
                if tempfuse.HasWarnings():
                    if(0>max_attempt_value):
                        max_attempt_value = 0
                else:
                    return [1, tempfuse]
            except:
                return [-1, tempfuse]
        return[max_attempt_value, tempfuse]
        
    def fix3(): # tries adjusting the point by an infinitesimal amount in each direction (+/- 0.01), then fusing.
        max_attempt_value = -1 #-1 if error, 0 if warning, 1 if success
        p1copy = gp_Pnt(p1.X(), p1.Y(), p1.Z())
        p2copy = gp_Pnt(p2.X(), p2.Y(), p2.Z())
        tests = [['p1copy.SetX(p1copy.X()+0.01)', 'p1copy.SetX(p1copy.X()-0.01)'],
        ['p1copy.SetY(p1copy.Y()+0.01)', 'p1copy.SetY(p1copy.Y()-0.01)'],
        ['p1copy.SetZ(p1copy.Z()+0.01)', 'p1copy.SetZ(p1copy.Z()-0.01)'],
        ['p2copy.SetX(p2copy.X()+0.01)', 'p2copy.SetX(p2copy.X()-0.01)'],
        ['p2copy.SetY(p2copy.Y()+0.01)', 'p2copy.SetY(p2copy.Y()-0.01)'],
        ['p2copy.SetZ(p2copy.Z()+0.01)', 'p2copy.SetZ(p2copy.Z()-0.01)']]
        for item in tests:
            cylinder = pipe_segment(p1copy, p2copy, radius+0.001)
            eval(item[0])
            try:
                tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder)
                if tempfuse.HasWarnings():
                    if(0>max_attempt_value):
                        max_attempt_value=0
                        eval(item[1])
                else:
                    eval(item[1])
                    return [1, tempfuse]
            except:
                eval(item[1])
        return [max_attempt_value, tempfuse]
    
    config = get_app().values.config_values
    threading_depth = config.get("CONFIG_CHANNELS_THREADING_DEPTH")
    threading_radius = config.get("CONFIG_CHANNELS_THREADING_DIAMETER")/2
    for i in range(1, len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        cylinder = pipe_segment(p1, p2, radius)

        if(p1.Z()>0 and p2.Z()<0):
            if(threading_depth !=0 and threading_radius !=0):
                rize = p1.Z()-p2.Z()
                xsol = p1.X()
                ysol = p1.Y()
                #if the x or y value of the 2 points is not matching
                if(p1.X()!=p2.X()):
                    runx = p1.X()-p2.X()
                    mx = rize/runx
                    bx = p1.Z()-mx*p1.X()
                    xsol = -bx/mx
                if(p1.Y()!=p2.Y()):
                    runy = p1.Y()-p2.Y()
                    my = rize/runy
                    by = p1.Z()-my*p1.Y()
                    ysol = -by/my
                #cylinder at position where the pipe meets the xy axis for threading
                pa = gp_Pnt(xsol, ysol, -1)
                pb = gp_Pnt(xsol, ysol, 1)
                direction = helper.get_direction(pa, pb) #gives normalised pb-pa vector
                cylinder1 = BRepPrimAPI_MakeCylinder(gp_Ax2(pa, direction), threading_radius, threading_depth+1).Shape()#+1 since starts at -1
                try:
                    tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder1)
                    if(tempfuse.HasWarnings):
                        pass
                        # log.error("warning thrown while constructing threading") #seems to run every time so removed for the time being
                        # but will leave in as a comment for future bug finding
                    pipe = tempfuse.Shape()
                except Exception as e:
                    log.error("Failed constriction of needle threading"+str(e))

        try:
            tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder)
            if tempfuse.HasWarnings():
                fix = fix1()#tries adjusting the radius a bit (0.001)
                if(fix[0]==1):
                    tempfuse = fix[1]
                else:
                    fix = fix2()#tries rounding decimals =4,3,2
                    if(fix[0]==1):
                        tempfuse = fix[1]
                    else:
                        fix = fix3() #tries moving the point by +/- 0.001 in each direction.
                        if(fix[0]==1):
                            tempfuse = fix[1]
                        else:
                            printpoint(p1)
                            printpoint(p2)
                            log.warning("\n\n\n\n\n\n\n\n\n\nWarning thrown while constructing channel")
                            window.channel_display_warning()
                
        except:
            fix = fix1()
            if(fix[0]==1 or fix[0] ==0):
                tempfuse = fix[1]
            else:
                fix = fix2(p1,p2,radius)
                if(fix[0]==1 or fix[0] ==0):
                    tempfuse = fix[1]
                    if(fix[0] ==0):
                        fix = fix3()
                        if(fix[0]==1):
                            tempfuse = fix[1]
                        else:
                            printpoint(p1)
                            printpoint(p2)
                            log.warning("Warning sent while making 3d model of channel")
                            window.channel_display_warning()
                else:
                    fix = fix3()
                    if(fix[0]==1 or fix[0] ==0):
                        tempfuse = fix[1]
                        if(fix[0] ==0):
                            printpoint(p1)
                            printpoint(p2)
                            log.warning("Warning sent while making 3d model of channel")
                            window.channel_display_warning()
                    else:
                        printpoint(p1)
                        printpoint(p2)
                        log.error("loading channel to 3d display failed")
                        window.channel_display_error()


        pipe = tempfuse.Shape()

    try:
        for point in points[1:len(points)]:
            #BRepPrimAPI_MakeSphere makes a sphere centered at point and then makes it radius = radius
            temp = BRepAlgoAPI_Fuse(pipe, BRepPrimAPI_MakeSphere(point, radius).Shape())
            if(temp.HasWarnings):
                if(temp.HasWarnings):
                    temp = BRepAlgoAPI_Fuse(pipe, BRepPrimAPI_MakeSphere(point, radius-0.01).Shape())
                    if(temp.HasWarnings()):
                        log.error("Error Constructing corner of a 3D channel")
                        window.channel_display_error()
                    else:
                        pipe = temp.Shape()
                else:
                    pipe = temp.Shape()
            else:
                pipe = temp.Shape()
    except:
        window.channel_display_error()

    # if the points extend past z zero, don't extend
    if points[-1].Z() < 0:
        #if length == 2 and the last point in points has a Z value < 2 the for loop above will not have run and so there will be no threading added
        if(len(points)==2):
            threading_depth = config.get("CONFIG_CHANNELS_THREADING_DEPTH")
            threading_radius = config.get("CONFIG_CHANNELS_THREADING_DIAMETER")/2
            p1 = points[0]
            p2 = points[1]
            if(threading_depth !=0 and threading_radius !=0):
                rize = p1.Z()-p2.Z()
                xsol = p1.X()
                ysol = p1.Y()
                #if the x or y value of the 2 points is not matching
                if(p1.X()!=p2.X()):
                    runx = p1.X()-p2.X()
                    mx = rize/runx
                    bx = p1.Z()-mx*p1.X()
                    xsol = -bx/mx
                if(p1.Y()!=p2.Y()):
                    runy = p1.Y()-p2.Y()
                    my = rize/runy
                    by = p1.Z()-my*p1.Y()
                    ysol = -by/my
                #cylinder at position where the pipe meets the xy axis for threading
                pa = gp_Pnt(xsol, ysol, -1)
                pb = gp_Pnt(xsol, ysol, 1)
                direction = helper.get_direction(pa, pb) #gives normalised pb-pa vector
                cylinder1 = BRepPrimAPI_MakeCylinder(gp_Ax2(pa, direction), threading_radius, threading_depth+1).Shape()#+1 since starts at -1
                try:
                    tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder1)
                    if(tempfuse.HasWarnings):
                        pass
                        # log.error("warning thrown while constructing threading") #seems to run every time so removed for the time being
                        # but will leave in as a comment for future bug finding
                    pipe = tempfuse.Shape()
                except Exception as e:
                    log.error("Failed constriction of needle threading"+str(e))
        return pipe
    # extend out of cylinder
    extension_for_pipe = down_to_end(points[-1], radius)
    extended_pipe = BRepAlgoAPI_Fuse(pipe, extension_for_pipe).Shape()

    return extended_pipe

def _cone_pipe(p1, p2, radius: float) -> TopoDS_Shape:
    p2.SetX(p2.X()+0.01) # 0.01 makes it so the cone will never be perfectly perpendicular to the cylinder coming after it
                    # in the event there is a perfectly vertical needle channel
                    # (if 3 points are linearly related there seems to be an issue fusing cylinders together)
                    # In the event p3 is collinear p_mid and p2 as defined by the create_point function
                    # then that should be caught in fix3() when building the channel
    length = helper.get_magnitude(p1, p2) #gives vector p2 - p1 and then get the norm
    direction = helper.get_direction(p2, p1) #gives normalised p1-p2 vector 
    axis = gp_Ax2(p2, direction) # creates coordinate system with an origin at p2, and z- axis pointed in "direction"
    return BRepPrimAPI_MakeCone(axis, radius, 0.001, length).Shape() # Cone made with height = length, bottom radius = 0, top radius =radius, on the axis as defined in the previous line


def down_to_end(p1: gp_Pnt, radius: float) -> TopoDS_Shape:
    config = get_app().values.config_values
    threading_depth = config.get("CONFIG_CHANNELS_THREADING_DEPTH")
    threading_radius = config.get("CONFIG_CHANNELS_THREADING_DIAMETER")/2
    #if threading_radius or threading_depth = 0 then just generate end of needle as normal, else make channel
    if(threading_depth !=0 and threading_radius !=0):
        p2 = gp_Pnt(p1.X(), p1.Y(), threading_depth)#p2 will be placed at a z-value of threading_depth which will be the end of the channel going down to the base of the cylinder
        length = helper.get_magnitude(p1,p2)
        if(p1.Z()>threading_depth):
            direction = helper.get_direction(p1, p2) #gives normalised p2-p1 vector
            cylinder1 = BRepPrimAPI_MakeCylinder(gp_Ax2(p1, direction), radius, length+0.01).Shape()#+0.01 is so that the smaller cylinder extends into the larger cylinder for the threading a little bit so that they will merge without issue
            cylinder2 = BRepPrimAPI_MakeCylinder(gp_Ax2(p2, direction), threading_radius, threading_depth+1).Shape()#extends the threading 1 past the end of the cylinder so to help with merging
            cylinder = BRepAlgoAPI_Fuse(cylinder1, cylinder2).Shape()
            return cylinder# adds cylinder an sphere together
        else:
            direction = helper.get_direction(p1, gp_Pnt(p1.X(), p1.Y(),0)) #gives normalised (p1.X(), p1.Y(),0)-p1 vector
            cylinder2 = BRepPrimAPI_MakeCylinder(gp_Ax2(p2, direction), threading_radius, threading_depth+1).Shape()#extends the threading 1 past the end of the cylinder so to help with merging
            return cylinder2
    else:
        p2 = gp_Pnt(p1.X(), p1.Y(), -1)
        direction = helper.get_direction(p1, p2) #gives normalised p2-p1 vector
        length = helper.get_magnitude(p1,p2)

        cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(p1, direction), radius, length).Shape()
        return cylinder#tempfusedpipe.Shape() # adds cylinder an sphere together

def pipe_segment(p1: gp_Pnt, p2: gp_Pnt, radius: float) -> TopoDS_Shape:
    direction = helper.get_direction(p1, p2) #gives normalised p2-p1 vector
    length = helper.get_magnitude(p1,p2)
    cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(p1, direction), radius, length).Shape()
    return cylinder

def remove_identical_points(points):
    """Removes identical points from the list."""
    unique_points = []
    for point in points:
        if not unique_points or not np.allclose(point, unique_points[-1]):
            unique_points.append(point)
    return unique_points


def remove_collinear_points(points):
    def is_collinear(p1, p2, p3):
        """Check if three points are collinear"""
        # Create vectors
        v1 = np.array(p2) - np.array(p1)
        v2 = np.array(p3) - np.array(p2)
        if np.all(v1 == v2):
            return True

        # Calculate the dot product
        dot_product = np.dot(v1, v2)

        # Calculate the magnitude of the vectors
        magnitude_vector1 = np.linalg.norm(v1)
        magnitude_vector2 = np.linalg.norm(v2)
        

        # Calculate the cosine of the angle
        cos_angle = dot_product / (magnitude_vector1 * magnitude_vector2)

        # Calculate the angle in radians
        angle_radians = np.arccos(cos_angle)

        # Convert to degrees, if needed
        angle_degrees = np.degrees(angle_radians)

        parallel = angle_degrees < 0.02
        # print(is_close)
        return parallel

    # Handle lists with fewer than 3 points
    if len(points) < 3:
        return points

    filtered_points = [points[0]]
    last_point = points[0]
    for i in range(1, len(points) - 1):
        if not is_collinear(last_point, points[i], points[i + 1]):
            filtered_points.append(points[i])
            last_point = points[i]
    filtered_points.append(points[-1])

    return filtered_points


def create_point(p1, p2, radius):
    length = helper.get_magnitude(p1, p2)
    if length < TIP_LENGTH:
        pipe = _cone_pipe(p1, p2, radius)
    else:
        vector = helper.get_vector(p1, p2, length=TIP_LENGTH) #gives normalized vector of p2-p1 *TIP_LENGTH
        p_mid = gp_Pnt(p1.X() + vector.X(), p1.Y() +
                        vector.Y(), p1.Z() + vector.Z())
        cone = _cone_pipe(p1, p_mid, radius) #makes cone at end of needle
        pipe = pipe_segment(p_mid, p2, radius)
        temp = BRepAlgoAPI_Fuse(cone, pipe)
        pipe=temp.Shape()
        return (pipe,temp.HasWarnings)


def printpoint(p1: gp_Pnt):
    print("("+str(p1.X())+","+str(p1.Y())+","+str(p1.Z())+")")
