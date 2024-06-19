from PySide6.QtWidgets import QMainWindow, QMessageBox

from classes.logger import log
from classes.app import get_app
from windows.ui import main_window_ui
from windows.views.viewport import OrbitCameraViewer3d
from windows.models.display_model import DisplayModel
from windows.models.dicom_model import DicomModel
from windows.models.channels_model import ChannelsModel
from windows.models.cylinder_model import CylinderModel
from windows.models.tandem_model import TandemModel
from windows.models.navigation_model import NavigationModel

from classes.info import USER_PATH
import json

class MainWindow(QMainWindow):

    def __init__(self, *args):
        super().__init__(*args)

        app = get_app()
        self.initialized = False

        log.info("Starting main window initialization")

        # TODO load user settings

        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO set keyboard shortcuts
        # TODO set theme
        # TODO set window variables (name, title, position in monitor) 
        # TODO connect signals to events

        # view signals send the new page's index
        # TODO change the values to specific widgets?
        self.ui.btn_import_view.pressed.connect(lambda: app.signals.viewChanged.emit(0))
        self.ui.btn_cylinder_view.pressed.connect(lambda: app.signals.viewChanged.emit(1))
        self.ui.btn_channels_view.pressed.connect(lambda: app.signals.viewChanged.emit(2))
        self.ui.btn_tandem_view.pressed.connect(lambda: app.signals.viewChanged.emit(3))
        self.ui.btn_export_view.pressed.connect(lambda: app.signals.viewChanged.emit(4))

        
        self.ui.btn_import_view.pressed.connect(self.change_color_import)
        self.ui.btn_cylinder_view.pressed.connect(self.change_color_cylinder)
        self.ui.btn_channels_view.pressed.connect(self.change_color_channels)
        self.ui.btn_tandem_view.pressed.connect(self.change_color_tandem)
        self.ui.btn_export_view.pressed.connect(self.change_color_export)

        #app.signals.viewChanged.connect(self.ui.viewswidget.setCurrentIndex)

    def change_color_import(self):
        views = [self.ui.btn_import_view, self.ui.btn_cylinder_view, self.ui.btn_channels_view, self.ui.btn_tandem_view, self.ui.btn_export_view]
        for v in views:
            if(v != self.ui.btn_import_view):
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(0, 0, 0);\n"
                "	background-color: rgb(199, 219, 237);\n"
                "	border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(48, 88, 162);\n"
                "}\n"
                "QPushButton:pressed {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "}")
            else:
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(250, 250, 250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "	border: 0px solid;\n"
                "}")
    def change_color_cylinder(self):
        views = [self.ui.btn_import_view, self.ui.btn_cylinder_view, self.ui.btn_channels_view, self.ui.btn_tandem_view, self.ui.btn_export_view]
        for v in views:
            if(v != self.ui.btn_cylinder_view):
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(0, 0, 0);\n"
                "	background-color: rgb(199, 219, 237);\n"
                "	border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(48, 88, 162);\n"
                "}\n"
                "QPushButton:pressed {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "}")
            else:
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(250, 250, 250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "	border: 0px solid;\n"
                "}")
    def change_color_channels(self):
        views = [self.ui.btn_import_view, self.ui.btn_cylinder_view, self.ui.btn_channels_view, self.ui.btn_tandem_view, self.ui.btn_export_view]
        for v in views:
            if(v != self.ui.btn_channels_view):
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(0, 0, 0);\n"
                "	background-color: rgb(199, 219, 237);\n"
                "	border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(48, 88, 162);\n"
                "}\n"
                "QPushButton:pressed {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "}")
            else:
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(250, 250, 250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "	border: 0px solid;\n"
                "}")
    def change_color_tandem(self):
        views = [self.ui.btn_import_view, self.ui.btn_cylinder_view, self.ui.btn_channels_view, self.ui.btn_tandem_view, self.ui.btn_export_view]
        for v in views:
            if(v != self.ui.btn_tandem_view):
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(0, 0, 0);\n"
                "	background-color: rgb(199, 219, 237);\n"
                "	border: 0px solid;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(48, 88, 162);\n"
                "}\n"
                "QPushButton:pressed {\n"
                "	color: rgb(250,250,250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "}")
            else:
                v.setStyleSheet(u"QPushButton {\n"
                "	color: rgb(250, 250, 250);\n"
                "	background-color: rgb(28, 44, 81);\n"
                "	border: 0px solid;\n"
                "}")
    def change_color_export(self):
        app = get_app()
        dicom_file_opened = app.window.navigationmodel.views[0].dicom_file_opened
        if(dicom_file_opened):
            views = [self.ui.btn_import_view, self.ui.btn_cylinder_view, self.ui.btn_channels_view, self.ui.btn_tandem_view, self.ui.btn_export_view]
            for v in views:
                if(v != self.ui.btn_export_view):
                    v.setStyleSheet(u"QPushButton {\n"
                    "	color: rgb(0, 0, 0);\n"
                    "	background-color: rgb(199, 219, 237);\n"
                    "	border: 0px solid;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "	color: rgb(250,250,250);\n"
                    "	background-color: rgb(48, 88, 162);\n"
                    "}\n"
                    "QPushButton:pressed {\n"
                    "	color: rgb(250,250,250);\n"
                    "	background-color: rgb(28, 44, 81);\n"
                    "}")
                else:
                    v.setStyleSheet(u"QPushButton {\n"
                    "	color: rgb(250, 250, 250);\n"
                    "	background-color: rgb(28, 44, 81);\n"
                    "	border: 0px solid;\n"
                    "}")
        
        
    def initModels(self):
        # TODO initialize models
        self.displaymodel = DisplayModel()
        self.dicommodel = DicomModel()
        self.cylindermodel = CylinderModel()
        self.channelsmodel = ChannelsModel()
        self.tandemmodel = TandemModel()

        # TODO connect models to signals
        self.dicommodel.values_changed.connect(self.cylindermodel.load_data)
        self.dicommodel.values_changed.connect(self.channelsmodel.load_data)

        app = get_app()
        app.signals.height_changed.connect(self.channelsmodel.update_height_offset)
        app.signals.height_changed.connect(self.tandemmodel.update_height_offset)

    def initViews(self):
        # initialize canvas
        self.canvas = OrbitCameraViewer3d()
        self.ui.display_view_widget.layout().addWidget(self.canvas)
        self.canvas.InitDriver()
        self.display = self.canvas._display

        self.display.display_triedron()
        self.display.FitAll()

        self.displaymodel.shapes_changed.connect(self.canvas.update_display)

        # TODO views
        self.navigationmodel = NavigationModel()

        # show this window with resizing to ensure canvas is displayed properly
        self.showWithCanvas()  # shows and then resizes the window to properly display canvas
        self.initialized = True

        log.info("main window initialization complete")

    def showWithCanvas(self):
        # for the canvas widget to properly fit, we need to shrink the window slightly and then 
        # set it to the size as before
        size = [self.size().width(), self.size().height()]
        self.resize(size[0] - 1, size[1] - 1)  
        self.show()
        self.resize(size[0], size[1])
        
    # Show a message pop up to show which config values have been loaded, and if any default values were uesed
    def configLoadMessageBox(self, text: str):
        dialog = QMessageBox()
        dialog.setWindowTitle("Notification")
        dialog.setText(text) 
        dialog.setIcon(QMessageBox.Icon.Information)
        dialog.exec()

    def pdf_save_error(self):
        dialog = QMessageBox()
        dialog.setText("Your PDF was not saved, this may be because a pdf with the same name is open in another application. If this is the case please close the pdf and try exporting again.")
        dialog.setWindowTitle("PDF save error")
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.exec()


    def channel_display_warning(self):
        dialog = QMessageBox()
        dialog.setText("Warning thrown while constructing needle channels. Please inspect the export view to ensure the needle channels look the way they should. \nIf a needle does not look the way it should, check to ensure there is no mistake in the plan, or replace the points on the needle that are not displaying properly.")
        dialog.setWindowTitle("Warning")
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.exec()

    def channel_display_error(self):
        dialog = QMessageBox()
        dialog.setText("Error thrown while constructing channels. This indicates that there is likely a mistake in the 3D construction of your plan so please inspect the export view to ensure the needle channels look the way they should. Check to ensure there is no mistake in the plan, or replace the points on the needle that are not displaying properly.")
        dialog.setWindowTitle("Warning")
        dialog.setIcon(QMessageBox.Icon.Critical)
        dialog.exec()

    def single_point_pop_up_Nucleatron(self):
        dialog = QMessageBox()
        dialog.setText("Warning: at least two of your channels contain only a single point. If you intend to use these points as anchoring points please ensure that either: \n1. none of your anchoring points have a channel number nor a label,\nOR\n2. all of your anchoring points have a channel number and a label.")
        dialog.setWindowTitle("Multiple Anchoring Points")
        dialog.setIcon(QMessageBox.Icon.Warning)

        dialog.exec()

    def single_point_pop_up_Varian(self):
        dialog = QMessageBox()
        dialog.setText("Warning, at least one channel with a single point was detected, this point WILL NOT be included in the 3D model.")
        dialog.setWindowTitle("Channel with Single Point Detected")
        dialog.setIcon(QMessageBox.Icon.Warning)

        dialog.exec()
        
    def tandem_import_wrong_filetype_error(self):
        dialog = QMessageBox()
        dialog.setText("Please use a step file if importing a tandem.")
        dialog.setWindowTitle("Tandem Import Error")
        dialog.setIcon(QMessageBox.Icon.Warning)

        dialog.exec()
        
    def save_file_paths(self):
        """
        Saves the filepaths to config files in a .json dictionary called filepaths.json.
        """
        # create the dictionary that we want to save.
        app = get_app()
        most_recently_opened_config_file = app.values.most_recently_opened_config_file
        most_recently_saved_config_file = app.values.most_recently_saved_config_file
        filePathsDict = {
            "most_recently_opened_config_file": most_recently_opened_config_file,
            "most_recently_saved_config_file": most_recently_saved_config_file
        }


        # the name of the file we want to save to.
        filename = USER_PATH.joinpath("filepaths.json")

        # Save dictionary as .json file
        with open(filename, "w") as outfile:
            json.dump(filePathsDict, outfile, indent=0)

        log.info("Successfully saved filepaths.")

    def closeEvent(self, event):
        """
        Rewrites the filepaths.json file before closing.
        Overloads the default closeEvent method for this QMainWindow.
        
        When user presses "exit" of the brachify main window, 
        then save all the most recent filepaths in a file called filepaths.json 
        before exiting the program.
        """
        self.save_file_paths()

    def tandem_error(self, code):
        dialog = QMessageBox()
        if(code == "diam"):
            dialog.setText("Error: The input for channel diameter is too large or too small. Channel diameter reset to previous value.")
            dialog.setWindowTitle("Tandem Diameter Error - Tandem Diameter Set to Previous Value")

        elif(code == "stopper"):
            dialog.setText("Error: The input for stopper diameter is too large or too small. Stopper diameter reset to previous value.")
            dialog.setWindowTitle("Tandem Stopper Diameter Error - Tandem Stopper Diameter Set to Previous Value")

        elif(code == 'angle'):
            dialog.setText("Error: The input for bend angle is too large or too small. Bend angle reset to previous value.")
            dialog.setWindowTitle("Tandem Bend Angle Error - Tandem Angle Set to Previous Value")

        elif(code == 'height'):
            dialog.setText("Error: The input for tandem height is too large or too small. Tandem height reset to previous value.")
            dialog.setWindowTitle("Tandem Height Error - Tandem Height Set to Previous Value")

        elif(code == 'radius'):
            dialog.setText("Error: The input for bend radius is too large or too small. Bend radius reset to previous value.")
            dialog.setWindowTitle("Tandem Bend Radius Error - Tandem Bend Radius Set to Previous Value")
        
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.exec()