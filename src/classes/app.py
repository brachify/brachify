
from PySide6.QtWidgets import QApplication

from classes.signals import AppSignals


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

            # TODO process args like autoloading a file or project

            # create the text for the pop-up window label
            text = "The following values were successfully loaded from config.json:\n"
            if len(self.config_keys_loaded[0]) < 1:
                text += "None\n\n"
            else:
                for name in self.config_keys_loaded[0]:
                    text += (
                        "{0:40}{1:10}".format(name, str(self.config_values.get(name)))
                    )
                    text += '\n'

            text += "\nThe following values were not found in config.json.  Default values used instead.\n"
            if len(self.config_keys_loaded[1]) < 1:
                text += "None\n\n"
            else:
                for name in self.config_keys_loaded[1]:
                    text += (
                        "{0:40}{1:10}".format(name, str(self.config_values.get(name)))
                    )
                    text += '\n'

                    
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