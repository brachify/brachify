from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.Core.Geom import Geom_BezierCurve
from OCC.Core.TColgp import TColgp_Array1OfPnt
from OCC.Core.gp import gp_Pnt, gp_Pln, gp_Dir, gp_Circ, gp_Ax2
from OCC.Core.gp import gp_Pnt, gp_Circ, gp_Ax2, gp_Dir
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCone
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.TopoDS import TopoDS_Shape
from Core.Models.NeedleChannel import NeedleChannel

import Application.BRep.Helper as helper

import numpy as np

def generate_fused(points):
    # creates three solids and fuses them together:
    # tip of channel to where the curve will begin
    # curved section
    # path to outside the channel

    # converting points array into gp_Pnt array
    p1 = gp_Pnt(points[0][0], points[0][1], points[0][2])
    p2 = gp_Pnt(points[-2][0], points[-2][1], points[-2][2])  # end of first straight path, start of curve
    p3 = gp_Pnt(points[-1][0], points[-1][1], points[-1][2])  # middle of curve
    p4 = gp_Pnt(points[-1][0], points[-1][1], points[-1][2] - 3.0)  # end of curve, start of second straight path
    p5 = gp_Pnt(points[-1][0], points[-1][1], -1.0)  # end of second straight path directly downwards

    # pipe 1
    radius = 1.60
    edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
    make_wire = BRepBuilderAPI_MakeWire(edge)
    make_wire.Build()
    wire = make_wire.Wire()

    direction = gp_Dir(
        p2.X() - p1.X(),
        p2.Y() - p1.Y(),
        p2.Z() - p1.Z()
    )
    circle = gp_Circ(gp_Ax2(p1, direction), radius)
    profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
    profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
    profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    pipe1 = BRepOffsetAPI_MakePipe(wire, profile_face).Shape()

    # pipe bend
    # curve joining two straight paths
    array = TColgp_Array1OfPnt(1, 3)
    array.SetValue(1, p2)
    array.SetValue(2, p3)
    array.SetValue(3, p4)
    bz_curve = Geom_BezierCurve(array)
    bend_edge = BRepBuilderAPI_MakeEdge(bz_curve).Edge()

    # assembling the path
    wire = BRepBuilderAPI_MakeWire(bend_edge).Wire()

    # profile
    direction = gp_Dir(
        p3.X() - p2.X(),
        p3.Y() - p2.Y(),
        p3.Z() - p2.Z()
    )
    circle = gp_Circ(gp_Ax2(p2, direction), radius)
    profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
    profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
    profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()

    pipe_bend = BRepOffsetAPI_MakePipe(wire, profile_face).Shape()

    # pipe 2
    edge = BRepBuilderAPI_MakeEdge(p4, p5).Edge()
    make_wire = BRepBuilderAPI_MakeWire(edge)
    make_wire.Build()
    wire = make_wire.Wire()

    direction = gp_Dir(
        p5.X() - p4.X(),
        p5.Y() - p4.Y(),
        p5.Z() - p4.Z()
    )
    circle = gp_Circ(gp_Ax2(p4, direction), radius)
    profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
    profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
    profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
    pipe2 = BRepOffsetAPI_MakePipe(wire, profile_face).Shape()

    # result
    result = BRepAlgoAPI_Fuse(pipe1, pipe_bend).Shape()
    return BRepAlgoAPI_Fuse(result, pipe2).Shape()


def generate_stacked_fused(points, diameter: float = 3.00):
    # ref: https://stackoverflow.com/questions/47163841/pythonocc-opencascade-create-pipe-along-straight-lines-through-points-profile
    # using the cylinders for the tube and spheres for the connections
    # convert [x, y, z] to gp_Pnt(x, y, z)
    array = []
    for point in points:
        array.append(gp_Pnt(point[0], point[1], point[2]))
    array.append(gp_Pnt(points[-1][0], points[-1][1], -1.0))

    # generate cylinders
    pipes = []
    for i in range(len(array) - 1):
        edge = BRepBuilderAPI_MakeEdge(array[i], array[i + 1]).Edge()
        makeWire = BRepBuilderAPI_MakeWire(edge)
        makeWire.Build()
        wire = makeWire.Wire()

        direction = gp_Dir(
            array[i + 1].X() - array[i].X(),
            array[i + 1].Y() - array[i].Y(),
            array[i + 1].Z() - array[i].Z()
        )
        circle = gp_Circ(gp_Ax2(array[i], direction), diameter / 2)
        profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
        profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
        profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
        pipes.append(BRepOffsetAPI_MakePipe(wire, profile_face).Shape())

    # fuse pipes with a sphere at each joining point
    pipe = pipes[0]
    for i in range(len(array) - 1):
        sphere = BRepPrimAPI_MakeSphere(array[i], diameter / 2).Shape()
        pipe = BRepAlgoAPI_Fuse(pipe, sphere).Shape()
        pipe = BRepAlgoAPI_Fuse(pipe, pipes[i]).Shape()

    return pipe

def generate_curved_channel(channel: NeedleChannel, cylinder_offset: float, diameter: float = 3.0) -> TopoDS_Shape:
    '''
    Generates a TopoDS_Shape from the Needle Channel's points
    Cylinder Offset is for height offset
    diameter is the channel's diameter
    '''
    # offset points using z axis and cylinder's offset
    # and convert into a gp_Pnt
    points = []
    for point in channel.points:
        points.append(gp_Pnt(point[0], point[1], point[2] - cylinder_offset))
    
    radius = diameter /2 
    
    # generate starting point on top (cone)
    p1 = points[0]
    p2 = points[1]
    vector = np.array([channel.points[1][0], channel.points[1][1], channel.points[1][2]]) \
        - np.array([channel.points[0][0], channel.points[0][1], channel.points[0][2]])
    length = np.linalg.norm(vector)
    direction = helper.get_direction(p1, p2)
    axis = gp_Ax2(p1, direction)
    pipe = BRepPrimAPI_MakeCone(axis, 0.0, radius, length).Shape()
    face = helper.get_lowest_face(pipe)
    
    # for each (after the first), create a sphere and cylinder to next point to join
    for i in range(1, len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        
        edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
        makeWire = BRepBuilderAPI_MakeWire(edge)
        makeWire.Build()
        wire = makeWire.Wire()
        cylinder = BRepOffsetAPI_MakePipe(wire, face).Shape()
        pipe = BRepAlgoAPI_Fuse(pipe, cylinder).Shape()
        face = helper.get_lowest_face(cylinder)

    # add a curved pipe downwards using offset length and direction of last two points
    vector = helper.get_vector(points[-2], points[-1], length)
    p1 = points[-1]
    p2 = gp_Pnt(p1.X() + vector.X(), p1.Y() + vector.Y(), p1.Z() + vector.Z())
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
    
    # shape using last face
    pipe_bend = BRepOffsetAPI_MakePipe(wire, face).Shape()
    pipe = BRepAlgoAPI_Fuse(pipe, pipe_bend).Shape()
    
    return pipe
    # add a cylinder from pipe to past bottom of cylinder 
    
# def generate_fused(points):
#     # creates three solids and fuses them together:
#     # tip of channel to where the curve will begin
#     # curved section
#     # path to outside the channel

#     from OCC.Core.gp import gp_Pnt, gp_Pln, gp_Dir, gp_Circ, gp_Ax2

#     # converting points array into gp_Pnt array
#     p1 = gp_Pnt(points[0][0], points[0][1], points[0][2])
#     p2 = gp_Pnt(points[-2][0], points[-2][1], points[-2][2])  # end of first straight path, start of curve
#     p3 = gp_Pnt(points[-1][0], points[-1][1], points[-1][2])  # middle of curve
#     p4 = gp_Pnt(points[-1][0], points[-1][1], points[-1][2] - 3.0)  # end of curve, start of second straight path
#     p5 = gp_Pnt(points[-1][0], points[-1][1], -1.0)  # end of second straight path directly downwards

#     # pipe 1
#     radius = 1.60
#     edge = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
#     makeWire = BRepBuilderAPI_MakeWire(edge)
#     makeWire.Build()
#     wire = makeWire.Wire()

#     direction = gp_Dir(
#         p2.X() - p1.X(),
#         p2.Y() - p1.Y(),
#         p2.Z() - p1.Z()
#     )
#     circle = gp_Circ(gp_Ax2(p1, direction), radius)
#     profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
#     profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
#     profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
#     pipe1 = BRepOffsetAPI_MakePipe(wire, profile_face).Shape()

#     # pipe bend
#     # curve joining two straight paths
#     array = TColgp_Array1OfPnt(1, 3)
#     array.SetValue(1, p2)
#     array.SetValue(2, p3)
#     array.SetValue(3, p4)
#     bz_curve = Geom_BezierCurve(array)
#     bend_edge = BRepBuilderAPI_MakeEdge(bz_curve).Edge()

#     # assembling the path
#     wire = BRepBuilderAPI_MakeWire(bend_edge).Wire()

#     # profile
#     direction = gp_Dir(
#         p3.X() - p2.X(),
#         p3.Y() - p2.Y(),
#         p3.Z() - p2.Z()
#     )
#     circle = gp_Circ(gp_Ax2(p2, direction), radius)
#     profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
#     profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
#     profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()

#     pipe_bend = BRepOffsetAPI_MakePipe(wire, profile_face).Shape()

#     # pipe 2
#     edge = BRepBuilderAPI_MakeEdge(p4, p5).Edge()
#     makeWire = BRepBuilderAPI_MakeWire(edge)
#     makeWire.Build()
#     wire = makeWire.Wire()

#     direction = gp_Dir(
#         p5.X() - p4.X(),
#         p5.Y() - p4.Y(),
#         p5.Z() - p4.Z()
#     )
#     circle = gp_Circ(gp_Ax2(p4, direction), radius)
#     profile_edge = BRepBuilderAPI_MakeEdge(circle).Edge()
#     profile_wire = BRepBuilderAPI_MakeWire(profile_edge).Wire()
#     profile_face = BRepBuilderAPI_MakeFace(profile_wire).Face()
#     pipe2 = BRepOffsetAPI_MakePipe(wire, profile_face).Shape()

#     # result
#     result = BRepAlgoAPI_Fuse(pipe1, pipe_bend).Shape()
#     return BRepAlgoAPI_Fuse(result, pipe2).Shape()