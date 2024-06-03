# object to store all the config and default values
from settings import load
from settings.load import DEFAULT_CONFIG_VALUES
from classes.info import USER_PATH
from classes.logger import log
from classes.app import get_app
import json

class Values():

    def saveFilePaths(self):
        
        pass

    def readConfigFilePaths(self):
        """
        Reads and writes a .json file that stores the filepaths for which config files were most recently used and saved.
        """  

        # Search in the location where the log is stored to find a .json file called filepaths.json.
        file_name = USER_PATH.joinpath("filepaths.json")

        try:
            # open, read, parse as dictionary, and close the filepaths.json file
            file = open(file_name)
            file_paths = json.load(file)
            file.close()       
            log.debug("Successfully loaded the filepaths.json file.")

        except:
            # if can't read default settings from filepaths.json file, then ??????
            log.debug("Couldn't read from filepaths.json.")

        # if the key does not exist, get() returns None.
        self.most_recently_opened_config_file = file_paths.get("most_recently_opened_config_file")
        self.most_recently_saved_config_file = file_paths.get("most_recently_saved_config_file")


    def resetAllValues(self, values_dict: dict):
        """
        Resets all values in spin boxes to the values in the given dictionary and applies them to the views.
        """
        app = get_app()

        # set all the spin box values and apply the changes
        """
        Steps:
        1. read the value from the dictionary
        2. set the spin box value
        3. apply the value
        """

        # Cylinder View values
        cylinder_diameter = values_dict.get("CONFIG_CYLINDER_DIAMETER")
        cylinder_length = values_dict.get("CONFIG_CYLINDER_LENGTH")
        app.window.navigationmodel.views[1].ui.spinbox_diameter.setValue(cylinder_diameter)
        app.window.navigationmodel.views[1].ui.spinbox_length.setValue(cylinder_length)
        app.window.navigationmodel.views[1].action_apply_settings() # apply the above settings

        # Channels View values
        channels_diameter = channels_diameter = values_dict.get("CONFIG_CHANNELS_DIAMETER")
        needle_length = channels_diameter = values_dict.get("CONFIG_NEEDLE_LENGTH")
        app.window.navigationmodel.views[2].ui.spinbox_diameter.setValue(channels_diameter)
        app.window.navigationmodel.views[2].ui.sb_needle_length.setValue(needle_length)
        app.window.navigationmodel.views[2].action_apply_settings() # apply the above settings
        # note for above: the needle lengths do not affect the view at all.  They are only used when
        # generating the .pdf Reference sheet.

        # Tandem View values
        tandem_tip_height = values_dict.get("CONFIG_TANDEM_TIP_HEIGHT")
        tandem_channel_diameter = values_dict.get("CONFIG_TANDEM_CHANNEL_DIAMETER")
        tandem_stopper_diameter = values_dict.get("CONFIG_TANDEM_STOPPER_DIAMETER")
        tandem_tip_angle = values_dict.get("CONFIG_TANDEM_TIP_ANGLE")
        tandem_bend_radius = values_dict.get("CONFIG_TANDEM_BEND_RADIUS")

        app.window.navigationmodel.views[3].ui.sb_tandem_height.setValue(tandem_tip_height)
        app.window.navigationmodel.views[3].ui.sp_channel_diameter.setValue(tandem_channel_diameter)
        app.window.navigationmodel.views[3].ui.sp_stopper_diameter.setValue(tandem_stopper_diameter)
        app.window.navigationmodel.views[3].ui.sp_bend_angle.setValue(tandem_tip_angle)
        app.window.navigationmodel.views[3].ui.sb_bend_radius.setValue(tandem_bend_radius)

        # if there is a tandem already generated, update its values.  If not, don't generate one.
        # if tandem exists
        if app.window.tandemmodel._base_shape: # FIND A NEW WAY TO DO THIS BC OF _ AT BEGINNING****************************
            # if tandem is generated rather than imported
            if not app.window.tandemmodel.is_shape_imported:
                # apply the config settings
                app.window.navigationmodel.views[3].action_set_tandem()



    def createConfigMessageText(self):
        """
        Generates the string that is printed to the pop-up window to notify user of which values
        were successfully loaded from the config.json file, and which use the default values.
        """
        # create the text for the pop-up window label
        text = "The following values were successfully loaded from config.json:\n"
        if len(self.config_keys_loaded[0]) < 1:
            text += "None\n\n"
        else:
            for name in self.config_keys_loaded[0]:
                text += (
                    f"{name}   =   {str(self.config_values.get(name))}"
                )
                text += '\n'

        text += "\nThe following values were not found in config.json:\n(Default values used instead.)\n"
        if len(self.config_keys_loaded[1]) < 1:
            text += "None\n\n"
        else:
            for name in self.config_keys_loaded[1]:
                text += (
                    f"{name}   =   {str(self.config_values.get(name))}"
                )
                text += '\n'

        return text

    def __init__(self):
        # defines app.values.DEFAULT_CONFIG_VALUES from the load.py.
        # create an attribute of app that contains a dictionary of DEFAULT_CONFIG_VALUES.
        # these are to be used if config values cannot be pulled from a .json file on the user's computer.
        self.DEFAULT_CONFIG_VALUES = DEFAULT_CONFIG_VALUES
        
        # read the default settings from the config.json file, as a dictionary,
        # and store it in an attribtue called config_values so it can be accessed later.
        load_config_file_tuple = load.load_config_file()
        self.config_values = load_config_file_tuple[0]

        # store the list of which config values were successfully loaded or not.
        self.config_keys_loaded = load_config_file_tuple[1]

