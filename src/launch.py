from PySide6.QtWidgets import QApplication

import sys

from classes import info
from classes.logger import log
from settings.load import load_config_file, DEFAULT_CONFIG_VALUES

app = None


def main():
    global app

    # TODO parse command-line arguements
    # TODO process arguements

    log.info(f"Loaded modules from: {info.DIR_PATH}")

    from classes.app import RadiotherapyApp

    argv = [sys.argv[0]]

    try:
        app = RadiotherapyApp(argv)
    except Exception:
        # TODO show errors from within app
        log.critical("Radiotherapy App failed to load!")
        input("Press enter key to continue...")

    app.setApplicationName(info.APP_NAME)
    app.setApplicationVersion(info.APP_VERSION)

    # create an attribute of app that contains a dictionary of DEFAULT_CONFIG_VALUES
    # these are to be used if config values cannot be pulled from a .json file on the user's computer
    app.DEFAULT_CONFIG_VALUES = DEFAULT_CONFIG_VALUES

    # read the default settings from the config.json file, as a dictionary,
    # and store it in an attribtue called config_values so it can be accessed later.
    load_config_file_tuple = load_config_file()
    app.config_values = load_config_file_tuple[0]
    # store the list of which config values were successfully loaded or not.
    app.config_keys_loaded = load_config_file_tuple[1]

    # launch GUI
    if app.gui():

        # close the splash screen if any
        try:
            import pyi_splash
            pyi_splash.close()
            app.window.activateWindow()
        except:
            pass

        sys.exit(app.exec())


if __name__ == "__main__":
    main()
