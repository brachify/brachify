from PySide6.QtWidgets import QApplication

import sys

from classes import info
from classes.logger import log

app = None


def main():
    global app

    # TODO parse command-line arguements
    # TODO process arguements

    log.info(f"Loaded modules from: {info.DIR_PATH}")

    from classes.app import RadiotherapyApp

    argv = [sys.argv[0]]
    print("len of sys.argv = ", len(sys.argv))

    filepath_to_open_to = None
    if len(sys.argv) > 1: # This indicates brachify was launched from brachify-optimization
        filepath_to_open_to = str(sys.argv[1])

    try:
        app = RadiotherapyApp(argv)
    except Exception:
        # TODO show errors from within app
        log.critical("Radiotherapy App failed to load!")
        input("Press enter key to continue...")

    app.setApplicationName(info.APP_NAME)
    app.setApplicationVersion(info.APP_VERSION)

    # launch GUI
    if app.gui():

        # close the splash screen if any
        try:
            import pyi_splash # type: ignore # this package is part of PyInstaller and cannot be installed by a package manager. "type: ignore" suppresses type checking warnings on this line.
            pyi_splash.close()
            app.window.activateWindow()
        except:
            pass

        if filepath_to_open_to is not None: # if we want to open to a filepath immediately
            app.window.navigationmodel.views[0].action_import_dicom_folder(filepath_to_open_to)
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
