from PySide6.QtWidgets import QWidget, QFileDialog

from classes.app import get_app
from classes.logger import log
from windows.models.shape_model import ShapeTypes
from windows.ui.tandem_view_ui import Ui_Tandem_View
from windows.views.custom_view import display_action, CustomView

materials = {
    ShapeTypes.CYLINDER: {"rgb": [0.8, 0.8, 0.8], "transparent": True},
    ShapeTypes.CHANNEL: {"rgb": [0.8, 0.8, 0.8], "transparent": True},
    ShapeTypes.TANDEM: {"rgb": [0.2, 0.55, 0.55], "transparent": False},
    ShapeTypes.SELECTED: {"rgb": [0.2, 0.8, 0.55], "transparent": True}
}


class TandemView(CustomView):

    @display_action
    def action_clear_tandem(self):
        log.debug(f"action: clearing tandem")
        self.tandemmodel.clear_tandem()

    @display_action
    def action_set_tandem(self):
        log.debug(f"action: generate a tandem")

        self.tandemmodel.set_tandem(
            tandem_diameter=self.ui.sp_channel_diameter.value(),
            stopper_diameter=self.ui.sp_stopper_diameter.value(),
            tip_angle=self.ui.sp_bend_angle.value(),
            bend_radius= self.ui.sb_bend_radius.value(),
            tandem_length= self.ui.sb_tandem_height.value()
        )

    @display_action
    def action_import_tandem(self):
        log.debug(f"action: import a tandem")
        # file dialog to choose file
        filename = QFileDialog.getOpenFileName(
            self, 'Select Tandem Tool Model', "", "Supported files (*.stl *.3mf *.obj *.stp *.step)")[0]

        if not filename:  # no folder selected?
            log.info("no valid filename selected for importing")
            return

        log.info(f"file {filename} has been selected")

        self.tandemmodel.import_tandem(filename)
        self.update_settings()

    @display_action
    def action_set_import_offset(self):
        # get the current value in the spin box
        offset = self.ui.sb_height_offset.value()
        # use the spin box value as the new height offset value
        self.tandemmodel.set_import_height_offset(offset)

    def on_close(self):
        log.debug(f"on view close")

    @display_action
    def on_open(self):
        log.debug(f"on view open")

        displaymodel = get_app().window.displaymodel
        displaymodel.set_materials(materials)
        self.tandemmodel.update_display()

        self.update_settings()

    def update_settings(self):
        log.debug(f"updating settings")
        tandem_diameter = self.tandemmodel.tandem_diameter
        self.ui.sp_channel_diameter.setValue(tandem_diameter)

        stopper_diameter = self.tandemmodel.stopper_diameter
        self.ui.sp_stopper_diameter.setValue(stopper_diameter)

        tip_angle = self.tandemmodel.tip_angle
        self.ui.sp_bend_angle.setValue(tip_angle)

        bend_radius = self.tandemmodel.bend_radius
        self.ui.sb_bend_radius.setValue(bend_radius)

        tandem_length = self.tandemmodel.tandem_length
        self.ui.sb_tandem_height.setValue(tandem_length)
        #self.ui.sb_height_offset.setValue(tandem_length)

        # set the spin box value of height offset to the value currently in use
        height_offset = self.tandemmodel.mesh_offset
        self.ui.sb_height_offset.setValue(height_offset)

        filepath = self.tandemmodel.filepath
        self.ui.label_5.setText(f"Model filepath:\n{filepath}")

    def __init__(self):
        super().__init__()
        self.ui = Ui_Tandem_View()  # the converted python file from the ui file
        self.ui.setupUi(self)
        self.tandemmodel = get_app().window.tandemmodel

        # signals and slots
        self.ui.btn_apply.pressed.connect(self.action_set_tandem)
        self.ui.btn_clear_generate.pressed.connect(self.action_clear_tandem)
        self.ui.btn_import.pressed.connect(self.action_import_tandem)
        self.ui.btn_clear_import.pressed.connect(self.action_clear_tandem)     
        self.ui.btn_apply_offset.pressed.connect(self.action_set_import_offset)

        self.update_settings()
