from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt, gp
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Extend.ShapeFactory import rotate_shape

class CylinderNotch:
    """
    A small shape at Z=0 to be used to mark the cylinder
    """

    def shape(self) -> TopoDS_Shape:
        # make the box shape
        start_x = self.radius - self.length
        point = gp_Pnt(start_x, 0.0, 0.0)
        box = BRepPrimAPI_MakeBox(point, self.length, self.width, self.height).Shape()

        # rotate the box along 0, 0, 1
        return rotate_shape(shape=box, axis=gp.OZ(), angle=self.rotation, unite="deg")
    
    def __init__(self, diameter):
        self.width = 0.5
        self.length = 2.0
        self.height = 0.5

        self.rotation = 270.0
        self.radius = diameter / 2

