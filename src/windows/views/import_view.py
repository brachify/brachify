from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QFont

from classes.app import get_app
from classes.logger import log
from classes.dicom.fileio import read_dicom_folder
from classes.dicom.data import DicomData
from windows.models.shape_model import ShapeTypes
from windows.ui.import_view_ui import Ui_Import_View
from windows.views.custom_view import display_action, CustomView

import json
from settings.load import load_config_file

from settings.reset import resetAllValues

materials = {
    ShapeTypes.CYLINDER: {"rgb": [0.2, 0.55, 0.55], "transparent": True},
    ShapeTypes.CHANNEL: {"rgb": [0.2, 0.55, 0.55], "transparent": True},
    ShapeTypes.TANDEM: {"rgb": [0.2, 0.55, 0.55], "transparent": True},
    ShapeTypes.SELECTED: {"rgb": [0.2, 0.55, 0.55], "transparent": True}
}


class ImportView(CustomView):

    def action_update_config_label(self, file_name):
        """
        Updates the config label on the Import view to display the file name of the current config file.
        If no config file was loaded, or if no values from it were used, then display "None".
        """
        app = get_app()
        # create the text for the pop-up window label
        text = "Config file currently loaded:\n"
        # If the file was not found, or if the file did not contain any valid keys, then print None.
        if len(app.values.config_keys_loaded[0]) < 1:
            text += " None\n\n"
        # If the file did contain at least 1 valid key, then print the file path.
        else:
            text += f"{file_name}"

        self.ui.label_config_info.setText(text)


    def action_import_config_file(self):

        file_name = QFileDialog.getOpenFileName(
            self, "Open config file", "", "(*.json)")[0]
        
        # if no .json file is selected, then return (cancel the import)
        if file_name == "": 
            """
              NOTE: the other action_import_* methods below return '' if user presses cancel, since they are 
              expecting a string.  This is why if not foldername: works for those, but it doesn't for here.
            """
            log.info("no valid filename selected for importing")
            return

        # if a .json file has been selected
        log.info(f"file {file_name} has been selected")


        app = get_app()
        # get the current values in use.
        alternate_dict = app.values.config_values
        # read in the file and store the values.
        # read the default settings from the .json file, as a dictionary,
        # and store it in an attribtue called config_values so it can be accessed later.
        load_config_file_tuple = load_config_file(file_name=file_name, alternate_dict=alternate_dict)
        app.values.config_values = load_config_file_tuple[0]
        # store the list of which config values were successfully loaded or not.
        app.values.config_keys_loaded = load_config_file_tuple[1]

        # Pop-up window to alert user to which values were successfully read and which had to revert to defaults.
        # create the text that is printed to the pop-up window.
        text = app.values.createConfigMessageText(file_name)
        # call the pop-up window.
        app.window.configLoadMessageBox(text=text)

        # reset all the values in the spin boxes and in the views.
        resetAllValues(app.values.config_values)

        app.values.most_recently_opened_config_file = file_name

        # this updates the label to show the filepath of the current config file.
        self.action_update_config_label(file_name)
        log.info("Successfully reset all the values and views.")
        
        


    def action_import_dicom_folder(self):
        foldername = QFileDialog.getExistingDirectoryUrl(
            self, "Open patient folder").toLocalFile()
        
        self.folder_name = foldername

        if not foldername:  # no folder selected?
            log.info("no valid filename selected for importing")
            return

        app = get_app()
        window = app.window

        log.info(f"file {foldername} has been selected")
        try:
            data = window.dicommodel.data.reset() # resets all the data in the dicom 
            window.displaymodel.reset() # resets all the data in the display
        except:
            log.error("Error: Unable to reset screen properly")
        data = read_dicom_folder(foldername)

        # Add patient and plan info to window
        
        #if dicom file has been opened then the export tap can open and the button will change color
        #else the button will not change color, see main (not related to not being able to go to the
        #export tab before importing a file, only for button color)
        self.dicom_file_opened = True

        window.dicommodel.update(data)
        window.displaymodel.set_transparent(True)
        
        app.signals.viewChanged.emit(4)
        window.change_color_export()

    def action_update_import_label(self, data:DicomData):
        alldata= "Folder: "+self.folder_name+"\n\nPatient and Plan Info\n"
        a = ("Patient ID:      \t\t")          + str(data.patient_id)+ "\n"
        b = ("Patient Name:    \t\t")          + str(data.patient_name)+ "\n"
        c = ("Plan ID:         \t\t")          + str(data.plan_label)+ "\n"
        d = ("Approval Status: \t\t")          + str(data.approval_status) + "\n"
        e = ("Operator:        \t\t")          + str(data.operator) + "\n\n"
        f = ("Channels Info")                  + "\n"
        for i in range(len(data.channels_labels)):
            f = f+(str(data.channels_labels[i]))+ ",  Channel: "+str(data.channel_numbers[i])+"\n"
        

        tandem = data.tandem_channel
        g = ("Tandem Label:  ")+str(tandem)
        
        
        alldata = alldata+a+b+c+d+e+f+g

        self.ui.label_file_info.setText(alldata)

    @display_action
    def on_open(self):
        log.debug(f"on view open")
        displaymodel = get_app().window.displaymodel
        displaymodel.set_materials(materials)

    def __init__(self):
        self.folder_name = ""
        self.dicom_file_opened = False
        super().__init__()
        self.ui = Ui_Import_View()
        self.ui.setupUi(self)

        # signals and slots
        self.ui.btn_import_folder.pressed.connect(self.action_import_dicom_folder)
        self.ui.btn_config_file.pressed.connect(self.action_import_config_file)

        window = get_app().window
        window.dicommodel.values_changed.connect(self.action_update_import_label)

