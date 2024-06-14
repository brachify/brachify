import numpy as np

from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.GeomAbs import GeomAbs_Plane
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopoDS import topods, TopoDS_Solid, TopoDS_Shape
from OCC.Core.gp import gp_Dir, gp_Ax2, gp_Pnt, gp_Vec
from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Extend.ShapeFactory import translate_shp
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeTorus

from classes.dicom.data import DicomData
from classes.logger import log
from classes.mesh.helper import face_is_plane, geom_plane_from_face
from classes.mesh.notch import CylinderNotch

from classes.app import get_app

# get config cylinder length from config file.  If can't read from dictionary, set to 160.0 and print a message to log.
config_values = get_app().values.config_values
"""CONFIG_CYLINDER_LENGTH = config_values.get("CONFIG_CYLINDER_LENGTH") 
if CONFIG_CYLINDER_LENGTH == None:
    log.debug(
        "Couldn't read CONFIG_CYLINDER_LENGTH from current config values.  Using default value 160.0 instead.")
    CONFIG_CYLINDER_LENGTH = 160.0"""

# get config cylinder diameter from config file.  If can't read from dictionary, set to 30.0 and print a message to log.
"""CONFIG_CYLINDER_DIAMETER = config_values.get("CONFIG_CYLINDER_DIAMETER") 
if CONFIG_CYLINDER_DIAMETER == None:
    log.debug(
        "Couldn't read CONFIG_CYLINDER_DIAMETER from current config values.  Using default value 30.0 instead.")
    CONFIG_CYLINDER_DIAMETER = 30.0"""

class BrachyCylinder:
    
    @staticmethod
    def default_length() -> float: return get_app().values.config_values.get("CONFIG_CYLINDER_LENGTH")

    def shape(self) -> TopoDS_Shape:
        if self._shape:
            return self._shape

        # cylinder references
        cylinder_axis = gp_Dir(0, 0, 1)
        cylinder_vector = gp_Ax2(gp_Pnt(0, 0, 0), cylinder_axis)
        cylinder = BRepPrimAPI_MakeCylinder(cylinder_vector, self.diameter / 2, self.length)

        # Our goal is to find the highest Z face and remove it
        z_max = -300.0

        # We have to work our way through all the faces to find the highest Z face so we can remove it for the shell
        face_explorer = TopExp_Explorer(cylinder.Shape(), TopAbs_FACE)
        while face_explorer.More():
            face = topods.Face(face_explorer.Current())
            if face_is_plane(face):
                a_plane = geom_plane_from_face(face)

                # We want the highest Z face, so compare this to the previous faces
                a_pnt_loc = a_plane.Location()
                z = a_pnt_loc.Z()
                if z > z_max:
                    z_max = z
                    top_face = face
            face_explorer.Next()

        # applying fillet to whole cylinder
        fillet = BRepFilletAPI_MakeFillet(cylinder.Shape())
        for e in TopologyExplorer(top_face).edges():
            fillet.Add(self.diameter / 2, e)
        fillet.Build()
        cylinder = fillet.Shape()
        if self.expand_base:
            cylinder = add_base(
                shape=cylinder, radius1=self.diameter / 2, radius2=12.0)
            
        if self.notch:
            cylinder = add_notch(cylinder, self.notch)

        return cylinder

    def setDiameter(self, diameter: float) -> None:
        self.diameter = diameter
        self._shape = None
        self._shape = self.shape()

    def setLength(self, length: float) -> None:
        self.length = length
        self._shape = None
        self._shape = self.shape()

    def enableBase(self, isBaseEnabled: bool) -> None:
        self.expand_base = isBaseEnabled
        self._shape = None
        self._shape = self.shape()

    def __init__(self, diameter: float = get_app().values.config_values.get("CONFIG_CYLINDER_DIAMETER"), expand_base: bool = False): 
        self.length = get_app().values.config_values.get("CONFIG_CYLINDER_LENGTH")
        self.diameter = diameter
        self.expand_base = expand_base
        self._shape = None
        self.notch = CylinderNotch()


def get_brachy_cylinder(data: DicomData) -> BrachyCylinder:
    # if cylinder contour is provided in dicom file, then read diameter from it
    try: 
        point1 = np.asarray(data.cylinder_contour[0])
        point2 = np.asarray(data.cylinder_contour[-1])
        difference = point2 - point1
        diameter = np.sqrt((difference[0]) ** 2 +
                        (difference[1]) ** 2 + (difference[2]) ** 2)
        diameter = round(diameter, 1)

        log.debug(f"Cylinder results: \n Diameter: {diameter}")
    # if cylinder contour is not provided, then set to default value
    except Exception as error_message: 
        diameter = get_app().values.config_values.get("CONFIG_CYLINDER_DIAMETER")
        log.debug(f"No Cylinder surface contour, or error reading:\nDiameter set to default:"+str(diameter))

    return BrachyCylinder(diameter=diameter)


def add_base(shape: TopoDS_Solid, radius1: float, radius2: float):
    # cylinder references
    cylinder_axis = gp_Dir(0, 0, 1)
    cylinder_vector = gp_Ax2(gp_Pnt(0, 0, 0), cylinder_axis)
    cylinder = BRepPrimAPI_MakeCylinder(
        cylinder_vector, radius1+radius2, radius2).Shape()
    torus = BRepPrimAPI_MakeTorus(radius1 + radius2, radius2).Shape()
    torus = translate_shp(torus, gp_Vec(0.0, 0.0, radius2))
    result = BRepAlgoAPI_Cut(cylinder, torus).Shape()
    return BRepAlgoAPI_Fuse(shape, result).Shape()

def add_notch(shape: TopoDS_Shape, notch: CylinderNotch):
    if not notch: return shape

    return BRepAlgoAPI_Cut(shape, notch.shape()).Shape()