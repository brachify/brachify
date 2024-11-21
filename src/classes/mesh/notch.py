from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt, gp
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Extend.ShapeFactory import rotate_shape
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse

class CylinderNotch:
    """
    A small 'L' shape at Z=0 to be used to mark the cylinder
    """

    def shape(self) -> TopoDS_Shape:
        # the box on the base
        # start_x_1 = self.radius - self.length
        # point1 = gp_Pnt(start_x_1, 0.0, 0.0)
        # box1 = BRepPrimAPI_MakeBox(point1, self.length, self.width, -self.height).Shape()
        # the box box on the cylinder edge (swap height and length)
        # start_x_2 = self.radius - self.height
        start_x_2 = self.radius
        point2 = gp_Pnt(start_x_2, 0, -self.height)
        notch = BRepPrimAPI_MakeBox(point2, self.height, self.width, self.length+self.height).Shape()

        # fuse the boxes to make an 'L' shape
        # notch = BRepAlgoAPI_Fuse(box1, box2).Shape()

        # rotate the notch along 0, 0, 1
        return rotate_shape(shape=notch, axis=gp.OZ(), angle=self.rotation, unite="deg")
    
    def __init__(self, diameter):
        self.width = 1.0
        self.length = 10
        self.height = 0.5

        self.rotation = 270.0
        self.radius = diameter / 2

