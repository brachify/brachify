
from settings import load
from classes.info import USER_PATH
from classes.logger import log
# from classes.app import get_app
import json
from classes.info import USER_PATH
from settings.defaults import DEFAULT_CONFIG_VALUES

# object to store all the config and default values
class Values():

    def saveFilePaths(self):
        
        pass

    def readConfigFilePaths(self):
        """
        Reads a .json file that stores the filepaths for which config files were most recently used and saved.
        """  

        # Search in the location where the log is stored to find a .json file called filepaths.json.
        file_name = USER_PATH.joinpath("filepaths.json")

        try:
            # open, read, parse as dictionary, and close the filepaths.json file
            file = open(file_name)
            file_paths = json.load(file)
            file.close()       
            log.debug("Successfully loaded the filepaths.json file.")
            # if the key does not exist, get() returns None.
            self.most_recently_opened_config_file = file_paths.get("most_recently_opened_config_file")
            self.most_recently_saved_config_file = file_paths.get("most_recently_saved_config_file")

        except:
            # if can't read default settings from filepaths.json file, then ??????
            log.debug("Couldn't read from filepaths.json.")
            self.most_recently_opened_config_file = None
            self.most_recently_saved_config_file = None






    def createConfigMessageText(self, file_name):
        """
        Generates the string that is printed to the pop-up window to notify user of which values
        were successfully loaded from the config.json file, and which use the default values.
        """
        # create the text for the pop-up window label
        text = "The following values were successfully loaded from the config file:\n"
        if len(self.config_keys_loaded[0]) < 1:
            text += "None\n\n"
        else:
            for name in self.config_keys_loaded[0]:
                text += (
                    f"{name}   =   {str(self.config_values.get(name))}"
                )
                text += '\n'

        text += "\nThe following values were not found in the config file:\n(Default values used instead.)\n"
        if len(self.config_keys_loaded[1]) < 1:
            text += "None\n\n"
        else:
            for name in self.config_keys_loaded[1]:
                text += (
                    f"{name}   =   {str(self.config_values.get(name))}"
                )
                text += '\n'

        text += "\nConfig file: \n" + f"{file_name}"

        return text

    def __init__(self):
        # defines app.values.DEFAULT_CONFIG_VALUES from the load.py.
        # create an attribute of app that contains a dictionary of DEFAULT_CONFIG_VALUES.
        # these are to be used if config values cannot be pulled from a .json file on the user's computer.
        self.DEFAULT_CONFIG_VALUES = DEFAULT_CONFIG_VALUES
        
        # define default values for the following attributes
        self.most_recently_opened_config_file = None
        self.most_recently_saved_config_file = None

        # initialize attributes that contian file paths to config files.
        self.readConfigFilePaths()

        # on start up, reload the most recently used config file.
        file_name = self.most_recently_opened_config_file


        # the location of the config file for start up.
        #file_name = USER_PATH.joinpath("config.json")

        # read the default settings from the config.json file, as a dictionary,
        # and store it in an attribtue called config_values so it can be accessed later.
        load_config_file_tuple = load.load_config_file(file_name=file_name, alternate_dict=DEFAULT_CONFIG_VALUES)
        self.config_values = load_config_file_tuple[0]

        # store the list of which config values were successfully loaded or not.
        self.config_keys_loaded = load_config_file_tuple[1]

