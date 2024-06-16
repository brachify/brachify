from OCC.Core.gp import gp, gp_Vec
from OCC.Extend.ShapeFactory import translate_shp, rotate_shape

from PySide6.QtCore import QObject, Signal

from classes.app import get_app
from classes.logger import log
from classes.mesh.channel import NeedleChannel
from classes.mesh.fileio import read_3d_file
from classes.mesh.helper import extend_bottom_face
from classes.mesh.tandem import Tandem
from windows.models.shape_model import ShapeModel, ShapeTypes

TANDEM_LABEL = "tandem_shape"

# Defaults
# get defaults from config file.  If can't read from dictionary, set to 4.0, 8.0, ...
config_values = get_app().values.config_values
CONFIG_TANDEM_CHANNEL_DIAMETER = config_values.get("CONFIG_TANDEM_CHANNEL_DIAMETER") 
if CONFIG_TANDEM_CHANNEL_DIAMETER == None:
    log.debug(
        "Couldn't read CONFIG_TANDEM_CHANNEL_DIAMETER from current config values.  Using default value 4.0 instead.")
    CONFIG_TANDEM_CHANNEL_DIAMETER = 4.0

CONFIG_TANDEM_STOPPER_DIAMETER = config_values.get("CONFIG_TANDEM_STOPPER_DIAMETER") 
if CONFIG_TANDEM_STOPPER_DIAMETER == None:
    log.debug(
        "Couldn't read CONFIG_TANDEM_STOPPER_DIAMETER from current config values.  Using default value 8.0 instead.")
    CONFIG_TANDEM_STOPPER_DIAMETER = 8.0

CONFIG_TANDEM_TIP_ANGLE = config_values.get("CONFIG_TANDEM_TIP_ANGLE") 
if CONFIG_TANDEM_TIP_ANGLE == None:
    log.debug(
        "Couldn't read CONFIG_TANDEM_TIP_ANGLE from current config values.  Using default value 30.0 instead.")
    CONFIG_TANDEM_TIP_ANGLE = 30.0

CONFIG_TANDEM_TIP_HEIGHT = config_values.get("CONFIG_TANDEM_TIP_HEIGHT") 
if CONFIG_TANDEM_TIP_HEIGHT == None:
    log.debug(
        "Couldn't read CONFIG_TANDEM_TIP_HEIGHT from current config values.  Using default value 129.0 instead.")
    CONFIG_TANDEM_TIP_HEIGHT = 129.0

CONFIG_TANDEM_BEND_RADIUS = config_values.get("CONFIG_TANDEM_BEND_RADIUS") 
if CONFIG_TANDEM_BEND_RADIUS == None:
    log.debug(
        "Couldn't read CONFIG_TANDEM_BEND_RADIUS from current config values.  Using default value 35.0 instead.")
    CONFIG_TANDEM_BEND_RADIUS = 35.0

class TandemModel(QObject):

    values_changed = Signal()

    def exists(self):
        # Returns True if the tandem has a _base_shape (ie, if there is a tandem currently in use, both generated or imported).
        # Returns False if the tandem does not have a _base_shape (ie, if there is no tandem currently in use).
        if self._base_shape is None:
            return False
        else:
            return True

    def clear_tandem(self):
        # remove tandem from the display
        self._base_shape = None
        self.filepath = None
        self.update()

    def import_tandem(self, filepath: str):
        self.filepath = filepath
        self._base_shape = read_3d_file(filepath)
        self.is_shape_imported = True
        self.update()

    def set_import_height_offset(self, height_offset: float):
        if self.mesh_offset == height_offset:
            return
        if not self.filepath:
            # if we have not imported a tandem yet, then do not offset height.
            # ie. cannot offset height of generated tandem, bc instead use "tandem height" under "generate" tab
            return

        self.mesh_offset = height_offset
        # tandem_length is the length of the tandem itself plus the offset
        self.tandem_length = CONFIG_TANDEM_TIP_HEIGHT + height_offset
        self.update()

    def set_tandem(self,
                   tandem_diameter: float, 
                   stopper_diameter: float,
                   tip_angle: float,
                   bend_radius: float,
                   tandem_length: float):

        log.debug(f"setting tandem")
        self.filepath = None
        self.is_shape_imported = False  # used to flag height offsets

        self.tandem_diameter = tandem_diameter
        self.stopper_diameter = stopper_diameter
        self.tip_angle = tip_angle
        self.bend_radius = bend_radius
        self.tandem_length = tandem_length

        self._generate_tandem()

        self._display_shape = self.raw_shape()

        self.update()

    def set_tandem_channel(self, channel: NeedleChannel):
        rotation = 0.0
        if channel:
            rotation = channel.get_rotation()
        self.rotation = rotation
        self.update_display()

    def imported_tandem_rotation(self, rotation):
        self.rotation = rotation
        self._display_shape = rotate_shape(shape=self._base_shape, axis=gp.OZ(), angle=rotation)
        self.update()

    def shape(self):
        if not self._base_shape:
            return None
        log.debug(f"shape offsets being applied")

        # if using an imported file, also apply the mesh's offset
        height_offset = self.height_offset
        if self.filepath:
            height_offset += self.mesh_offset

        # apply offsets
        offset = gp_Vec(0.0, 0.0, height_offset)
        rotation = self.rotation

        shape = rotate_shape(
            shape=self._base_shape, axis=gp.OZ(), angle=rotation)
        if self.is_shape_imported:
            shape = translate_shp(shape, offset)

        if self.filepath:
            shape = extend_bottom_face(shape)

        return shape

    def raw_shape(self):
        log.debug(f"display shape being generated")
        tandem = Tandem()

        tandem.tandem_diameter = self.tandem_diameter
        tandem.stopper_diameter = self.stopper_diameter
        tandem.tandem_angle = self.tip_angle
        tandem.bend_radius = self.bend_radius
        tandem.tandem_height = self.tandem_length

        tandem.cylinder_height = self.cylinder_length
        tandem.cylinder_diameter = self.cylinder_diameter

        rotation = self.rotation

        self._display_shape = rotate_shape(shape=tandem.tandem_shape(), axis=gp.OZ(), angle=rotation)
        return self._display_shape

    def update(self):
        log.debug(f"updating")
        self.values_changed.emit()
        self.update_display()

    def update_cylinder(self):
        log.debug("updating cylinder on tandem model")

        cylindermodel = get_app().window.cylindermodel
        self.cylinder_length = cylindermodel.cylinder.length
        self.cylinder_diameter = cylindermodel.cylinder.diameter

        if self._base_shape is None:
            return

        if not self.is_shape_imported:
            self._generate_tandem()

        self.update()

    def update_display(self):
        log.debug(f"update display")
        if not self._base_shape:
            self.displaymodel.remove_shape(TANDEM_LABEL)
            return

        shape = self.shape()
        if not shape:
            return

        shape_model = ShapeModel(
            label=TANDEM_LABEL, shape=shape, shape_type=ShapeTypes.TANDEM)

        self.displaymodel.add_shape(shape_model)

    def update_height_offset(self, height_offset: float):
        log.debug(f"updating tandem height offset to {height_offset}")
        self.height_offset = height_offset
        self.update()

    def _generate_tandem(self):
        tandem = Tandem()

        tandem.tandem_diameter = self.tandem_diameter
        tandem.stopper_diameter = self.stopper_diameter
        tandem.tandem_angle = self.tip_angle
        tandem.bend_radius = self.bend_radius
        tandem.tandem_height = self.tandem_length

        tandem.cylinder_height = self.cylinder_length
        tandem.cylinder_diameter = self.cylinder_diameter

        self._base_shape = tandem.generate_shape()

    def __init__(self) -> None:
        super().__init__()
        self._base_shape = None  # base shape before extending due to height offset
        self._display_shape = None  # used to show tandem in export view
        self.height_offset = 0.0
        self.rotation = config_values.get("CONFIG_TANDEM_ROTATION") 
        self.filepath = None
        self.mesh_offset = 0.0
        self.is_shape_imported = False

        # cylinder settings
        self.cylinder_length = 0
        self.cylinder_radius = 0

        # tandem settings
        self.tandem_diameter = CONFIG_TANDEM_CHANNEL_DIAMETER
        self.stopper_diameter = CONFIG_TANDEM_STOPPER_DIAMETER
        self.tandem_angle = CONFIG_TANDEM_TIP_ANGLE
        self.bend_radius = CONFIG_TANDEM_BEND_RADIUS
        self.tandem_length = CONFIG_TANDEM_TIP_HEIGHT

        # generated tandem settings
        self.tip_angle = CONFIG_TANDEM_TIP_ANGLE

        # signals and slots
        window = get_app().window
        window.channelsmodel.tandem_changed.connect(self.set_tandem_channel)
        window.cylindermodel.values_changed.connect(self.update_cylinder)

        # references
        self.displaymodel = window.displaymodel

    @staticmethod
    def get_label(): return TANDEM_LABEL
