from PySide6.QtWidgets import QWidget, QFileDialog

from classes.app import get_app
from classes.logger import log
from classes.dicom.fileio import read_dicom_folder
from classes.dicom.data import DicomData
from windows.models.shape_model import ShapeTypes
from windows.ui.import_view_ui import Ui_Import_View
from windows.views.custom_view import display_action, CustomView

materials = {
    ShapeTypes.CYLINDER: {"rgb": [0.2, 0.55, 0.55], "transparent": True},
    ShapeTypes.CHANNEL: {"rgb": [0.2, 0.55, 0.55], "transparent": True},
    ShapeTypes.TANDEM: {"rgb": [0.2, 0.55, 0.55], "transparent": True},
    ShapeTypes.SELECTED: {"rgb": [0.2, 0.55, 0.55], "transparent": True}
}


class ImportView(CustomView):

    def action_import_dicom_folder(self):
        foldername = QFileDialog.getExistingDirectoryUrl(
            self, "Open patient folder").toLocalFile()
        
        if not foldername:  # no folder selected?
            log.info("no valid filename selected for importing")
            return

        log.info(f"file {foldername} has been selected")

        data = read_dicom_folder(foldername)

        # Add patient and plan info to window
        app = get_app()
        window = app.window
        
        #if dicom file has been opened then the export tap can open and the button will change color
        #else the button will not change color, see main (not related to not being able to go to the
        #export tab before importing a file, only for button color)
        self.dicom_file_opened = True

        window.dicommodel.update(data)
        window.displaymodel.set_transparent(True)
        
        app.signals.viewChanged.emit(4)
        window.change_color_export()

    def action_update_import_label(self, data:DicomData):
        alldata="Patient and Plan Info:\n"
        a = "{:<30}".format("Patient ID: ")               + "\t"+str(data.patient_id)+ "\n"
        b = "{:<30}".format("Patient Name: ")             + "\t"+str(data.patient_name)+ "\n"
        c = "{:<30}".format("Plan ID: ")                  + "\t"+str(data.plan_label)+ "\n"
        d = "{:<30}".format("Approval Status: ")          + "\t"+str(data.approval_status) + "\n"
        e = "{:<30}".format("Operator: ")                 + "\t"+str(data.operator) + "\n\n"
        f = "{:<30}".format("Channels Info")                  + "\n"
        for i in range(len(data.channels_labels)):
            f = f+"{:<30}".format("Label: "+str(data.channels_labels[i]))+"\t Channel: "+str(data.channel_numbers[i])+"\n"
        
        #line below has not yet been tested, remove is there is an issue
        tandem = get_app().window.channelsmodel.tandem_channel
        g = "{:<30}".format("Tandem Label:")+"\t "+str(tandem)
        
        
        alldata = alldata+a+b+c+d+e+f+g
        #last = data.toString()
        self.ui.label_file_info.setText(alldata)

    @display_action
    def on_open(self):
        log.debug(f"on view open")
        displaymodel = get_app().window.displaymodel
        displaymodel.set_materials(materials)

    def __init__(self):
        self.dicom_file_opened = False
        super().__init__()
        self.ui = Ui_Import_View()
        self.ui.setupUi(self)

        # signals and slots
        self.ui.btn_import_folder.pressed.connect(self.action_import_dicom_folder)
        
        window = get_app().window
        window.dicommodel.values_changed.connect(self.action_update_import_label)

