from PySide6.QtWidgets import QApplication

import sys

from classes import info
from classes.logger import log
from settings.load import load_config_file

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

    # read the default settings from the config.json file, 
    # and store it in an attribtue called config_values so it can be accessed later.
    load_config_file_tuple = load_config_file()
    app.config_values = load_config_file_tuple[0]
    # store the list of which config values were successfully loaded or not.
    app.config_load_message = load_config_file_tuple[1]

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
