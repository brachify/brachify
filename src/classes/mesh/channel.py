import numpy as np
import math
'''
Not in current use, but were used for the Bezier method
from OCC.Core.Geom import Geom_BezierCurve
from OCC.Core.TColgp import TColgp_Array1OfPnt
'''
from OCC.Core.gp import gp_Pnt, gp_Ax2
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCylinder

'''
also for Bezier method
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakeSphere
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe
'''
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.TopoDS import TopoDS_Shape

import classes.mesh.helper as helper
from classes.logger import log

from classes.app import get_app


TIP_LENGTH = 2.5
# get default channel diameter from config file.  If can't read from dictionary, set to 3.0.
config_values = get_app().config_values
CONFIG_CHANNELS_DIAMETER = config_values.get("CONFIG_CHANNELS_DIAMETER", 3.0)


class NeedleChannel:

    @staticmethod
    def default_diameter() -> float: return CONFIG_CHANNELS_DIAMETER

    #setChannel function is not currently in use.  It is left here in case it is needed in the future.
    '''
    def setChannel(self, height: float = 0.0, diameter: float = 3.0) -> None:
        self._offset = height
        self._diameter = diameter
        self._shape = None
        self.shape()
    '''

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
    
    def __init__(self, number: str, label: str, points):
        self.number = number
        self.label = label
        self.points = points
        self.points_raw = points
        self._shape = None

        self._offset = 0.0
        self._diameter = CONFIG_CHANNELS_DIAMETER

def rounded_channel(channel_points, offset: float = 0.0, diameter: float = 3.0) -> TopoDS_Shape:
    
    """
    If a needle channel has a long distance between the first and second point, this helps stub it
    """
    ################################################
    # possibly remove this if statment later, there should never be a channel points that gets to this point with <2 points
    ################################################
    if len(channel_points) < 2:
        log.error(F"Needle Channel Generation error! needs 2 or more points!")
        return None
    # offset points using z axis and cylinder's offset
    # and convert into a gp_Pnt
    # rounding/truncation is needed otherwise there can be a bug in pipe = BRepAlgoAPI_Fuse(cone, pipe).Shape() below.

    channel_points = np.array(channel_points)
    
    # apply the offset for the cylinder length
    # all rows column 3
    channel_points[:,2] += offset

    # Number of decimal places to keep
    decimals = 5

    # Truncate without rounding
    channel_points = np.floor(channel_points * 10**decimals) / 10**decimals

    channel_points = remove_collinear_points(channel_points)
    
    points = [gp_Pnt(point[0], point[1], point[2]) for point in channel_points]

    radius = diameter / 2

    log.debug("Channel being constructed for 3d display")

    # generate starting point on top (cone)
    p1 = points[0]
    p2 = points[1]
    length = helper.get_magnitude(p1, p2)
    if length < TIP_LENGTH:
        pipe = _cone_pipe(p1, p2, radius)
    else:
        vector = helper.get_vector(p1, p2, length=TIP_LENGTH) #gives normalized vector of p2-p1 *TIP_LENGTH
        p_mid = gp_Pnt(p1.X() + vector.X(), p1.Y() +
                       vector.Y(), p1.Z() + vector.Z())
        cone = _cone_pipe(p1, p_mid, radius) #makes cone at end of needle
        pipe = _rounded_pipe(p_mid, p2, radius)
        pipe = BRepAlgoAPI_Fuse(cone, pipe).Shape()
        

    # rest of the points
    for i in range(1, len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        cylinder = _rounded_pipe(p1, p2, radius)
        try:
            tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder)
            # print(tempfuse.HasErrors())
            if tempfuse.HasWarnings():
                
                log.warning("warning sent while making 3d model of channel")
                # tempfuse = BRepAlgoAPI_Fuse(pipe, cylinder).SetFuzzyValue(0.00005)
                # print(tempfuse.HasWarnings())
                
            # print(tempfuse.HasWarnings())
            pipe = tempfuse.Shape()
        except:
            log.error("loading channel to 3d display failed")

    # if the points extend past z zero, don't extend
    if points[-1].Z() < 0:
        return pipe

    '''
    #original code
    # curve downwards
    curve = _curved_end(points, radius)
    pipe = BRepAlgoAPI_Fuse(pipe, curve).Shape()

    # extend out of cylinder
    face = helper.get_lowest_face(pipe)
    extended_pipe = _extended_pipe(pipe)
    '''
    # extend out of cylinder
    extension_for_pipe = down_to_end(points[-1], radius)
    extended_pipe = BRepAlgoAPI_Fuse(pipe, extension_for_pipe).Shape()

    return extended_pipe

def _cone_pipe(p1, p2, radius: float) -> TopoDS_Shape:
    length = helper.get_magnitude(p1, p2) #gives vector p2 - p1 and then get the norm
    direction = helper.get_direction(p1, p2) #gives normalised p2-p1 vector 
    axis = gp_Ax2(p1, direction) # creates coordinate system with an origin at p1, and z- axis pointed in "direction"
    return BRepPrimAPI_MakeCone(axis, 0.0, radius, length).Shape() # Cone made with height = length, bottom radius = 0, top radius =radius, on the axis as defined in the previous line
'''

def _straight_pipe(p1, p2, face) -> TopoDS_Shape:
    edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
    make_wire = BRepBuilderAPI_MakeWire(edge)
    make_wire.Build()
    wire = make_wire.Wire()
    return BRepOffsetAPI_MakePipe(wire, face).Shape()
'''

def down_to_end(p1: gp_Pnt, radius: float) -> TopoDS_Shape:
    p2 = gp_Pnt(p1.X(), p1.Y(), -1)
    direction = helper.get_direction(p1, p2) #gives normalised p2-p1 vector
    length = helper.get_magnitude(p1,p2)

    cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(p1, direction), radius, length).Shape()
    return cylinder#tempfusedpipe.Shape() # adds cylinder an sphere together

def _rounded_pipe(p1: gp_Pnt, p2: gp_Pnt, radius: float) -> TopoDS_Shape:
    direction = helper.get_direction(p1, p2) #gives normalised p2-p1 vector
    length = helper.get_magnitude(p1,p2)

    sphere = BRepPrimAPI_MakeSphere(p2, radius).Shape()# makes a sphere centered at p2 and then makes it radius = radius
    cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(p1, direction), radius, length).Shape()
    pipe_cylinder = BRepAlgoAPI_Fuse(cylinder, sphere).Shape()
    return pipe_cylinder#tempfusedpipe.Shape() # adds cylinder an sphere together

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
'''
    Original methods
    def _extended_pipe(shape: TopoDS_Shape) -> TopoDS_Shape:
    location = None

    lowest_face = helper.get_lowest_face(shape)
    if helper.face_is_plane(lowest_face):
        a_plane = helper.geom_plane_from_face(lowest_face)
        location = a_plane.Location()

    if location is None or location.Z() < 0:
        return shape

    extension = _straight_pipe(location, gp_Pnt(
        location.X(), location.Y(), -0.1), lowest_face)
    return BRepAlgoAPI_Fuse(shape, extension).Shape()


def _curved_end(points: list[gp_Pnt], radius: float) -> TopoDS_Shape:
    # add a curved pipe downwards using offset length and direction of last two points
    length = helper.get_magnitude(points[-2], points[-1])
    vector = helper.get_vector(points[-2], points[-1], length)
    p1 = points[-1]  # last point in array
    p2 = gp_Pnt(p1.X() + vector.X(), p1.Y() + vector.Y(),
                p1.Z() + vector.Z())  # middle point for bcurve
    # last point, lowered towards bottom
    p3 = gp_Pnt(p2.X(), p2.Y(), p2.Z() - length)

    # curve joining two straight paths
    array = TColgp_Array1OfPnt(1, 3)
    array.SetValue(1, p1)
    array.SetValue(2, p2)
    array.SetValue(3, p3)
    bz_curve = Geom_BezierCurve(array)
    bend_edge = BRepBuilderAPI_MakeEdge(bz_curve).Edge()

    # assembling the path
    wire = BRepBuilderAPI_MakeWire(bend_edge).Wire()

    # profile
    direction = helper.get_direction(p1, p2)
    profile = helper.circle_profile(p1, direction, radius)

    # shape using last face
    return BRepOffsetAPI_MakePipe(wire, profile).Shape()


def _rounded_pipe(p1: gp_Pnt, p2: gp_Pnt, radius: float) -> TopoDS_Shape:
    direction = helper.get_direction(p1, p2)
    profile = helper.circle_profile(p1, direction, radius)

    guide_edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
    guide_wire = BRepBuilderAPI_MakeWire(guide_edge).Wire()

    cylinder = BRepOffsetAPI_MakePipe(guide_wire, profile).Shape()
    sphere = BRepPrimAPI_MakeSphere(p2, radius).Shape()
'''