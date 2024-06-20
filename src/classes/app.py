
from PySide6.QtWidgets import QApplication

from classes.signals import AppSignals

from settings.values import Values

from PySide6.QtGui import QIcon

def get_app():
    """ Returns the current QApplication instance """
    return QApplication.instance()


class RadiotherapyApp(QApplication):

    def gui(self):
        """
        Initialize the GUI and the Main Window
        :return: bool: True if the GUI has no errors, False if initialization fails
        """

        try:
            from windows.main_window import MainWindow
            self.window = MainWindow()

            # these were seperated from the MainWindow __init__ to ease signal connections
            self.window.initModels()
            self.window.initViews()

            my_icon = QIcon("resources\\brachify_splash-ico.ico")
            self.window.setWindowIcon(my_icon)

            # TODO process args like autoloading a file or project
            
            # update the config label on the import view to display the info from the loaded config file.            
            file_name = self.values.most_recently_opened_config_file
            #(Need to figure out) text = self.values.createConfigMessageText(file_name, isFromUserImport=False)
            #self.window.navigationmodel.views[0].action_update_config_label(file_name, text)
            
            self.window.navigationmodel.views[0].action_update_config_label(file_name)

            # create the text that is printed to the pop-up window
            text = self.values.createConfigMessageText(file_name)
            # call the pop-up window
            self.window.configLoadMessageBox(text=text)

            return True
        
        except Exception as error_message:
            from classes.logger import log
            log.critical(f"Main window start failed: {error_message}")
            return False
    
    @property 
    def signals(self) -> AppSignals:
        return self._signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = super().arguments()
        self.errors = []
        self._signals = AppSignals()

        try:
            from classes.info import APP_NAME, DIR_PATH
            from classes.logger import log
            log.info(f"Starting {APP_NAME}")

        except ImportError as error_message:
            print(f"logging module unable to import! \n{error_message}")
            raise

        except Exception as error_message:
            print(f"Unable to start logging. \n{error_message}")
            raise

        self.path = DIR_PATH

        # attribute that contains config and default values
        self.values = Values()