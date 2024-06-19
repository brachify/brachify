
from settings import load
from classes.info import USER_PATH
from classes.logger import log
import json
from classes.info import USER_PATH
from settings.defaults import DEFAULT_CONFIG_VALUES

# object to store all the config and default values
class Values():

    def readConfigFilePaths(self):
        """
        Reads a .json file that stores the filepaths for which config files were most recently used and saved.
        """  

        # Search in the location where the log is stored to find a .json file called filepaths.json.
        file_name = USER_PATH.joinpath("filepaths.json")

        try:
            # open, read, parse as dictionary, and close the filepaths.json file
            with open(file_name) as file:
                file_paths = json.load(file)

            log.debug("Successfully loaded the filepaths.json file.")
            # if the key does not exist, get() returns None.
            self.most_recently_opened_config_file = file_paths.get("most_recently_opened_config_file")
            self.most_recently_saved_config_file = file_paths.get("most_recently_saved_config_file")

        except:
            # if can't read default settings from filepaths.json file
            log.debug("Couldn't read from filepaths.json.")
            self.most_recently_opened_config_file = None
            self.most_recently_saved_config_file = None






    def createConfigMessageText(self, file_name, isFromUserImport):
        """
        Generates the string that is printed to the pop-up window to notify user of which values
        were successfully loaded from the config.json file, and which use the default values.
        """    
        # create the text for the pop-up window label
        text = "Config file currently loaded:\n"
        # If the file was not found, or if the file did not contain any valid keys, then print None.
        if len(self.config_keys_loaded[0]) < 1:
            # if we had to use defaults, because no previous file had ever been successfully loaded
            if self.num_configs_loaded_successfully < 1:
                text += "None\n"
            # if we had to use previous values, because we had successfully used a previous file
            if self.num_configs_loaded_successfully >= 1:
                text += "Previous file\n"
        # If the file did contain at least 1 valid key, then print the file path.
        else:
            text += f"{file_name}"
            text += "\n"

        text += "\nThe following values were successfully loaded from the config file:\n"
        
        # if no config values were loaded from the file (ie we had to use all defaults or all previous values)
        if len(self.config_keys_loaded[0]) < 1:
            text += "None\n"
        else:
            for name in self.config_keys_loaded[0]:
                modified_name = name.removeprefix("CONFIG_").replace("_", " ").title()
                text += (
                    f"{modified_name}   =   {str(self.config_values.get(name))}"
                )
                text += '\n'

        text += "\nThe following values were not found in the config file:\n"
        text += f"({'Previous' if isFromUserImport else 'Default'} values used instead.)"
        text += "\n"
        if len(self.config_keys_loaded[1]) < 1:
            text += "None\n\n"
        else:
            for name in self.config_keys_loaded[1]:
                modified_name = name.removeprefix("CONFIG_").replace("_", " ").title()
                text += (
                    f"{modified_name}   =   {str(self.config_values.get(name))}"
                )
                text += '\n'

        #text += "\nConfig file: \n" + f"{file_name}"

        return text

    def __init__(self):
        # defines app.values.DEFAULT_CONFIG_VALUES from the load.py.
        # create an attribute of app that contains a dictionary of DEFAULT_CONFIG_VALUES.
        # these are to be used if config values cannot be pulled from a .json file on the user's computer.
        self.DEFAULT_CONFIG_VALUES = DEFAULT_CONFIG_VALUES
        
        # define default values for the following attributes
        self.most_recently_opened_config_file = None
            # the following value is saved in filepaths.json, but is not used otherwise. (future developement)
        self.most_recently_saved_config_file = None

        # define a counter to count the number of config files that we have been able to successfully
        # load 1 or more values from.
        self.num_configs_loaded_successfully = 0

        # initialize attributes that contian file paths to config files.
        self.readConfigFilePaths()

        # on start up, reload the most recently used config file.
        file_name = self.most_recently_opened_config_file

        # read the default settings from the config.json file, as a dictionary,
        # and store it in an attribtue called config_values so it can be accessed later.
        load_config_file_tuple = load.load_config_file(file_name=file_name,
                                                       alternate_dict=DEFAULT_CONFIG_VALUES, 
                                                       num_configs_loaded_successfully=self.num_configs_loaded_successfully)
        self.config_values = load_config_file_tuple[0]

        # store the list of which config values were successfully loaded or not.
        self.config_keys_loaded = load_config_file_tuple[1]

        # store whether 1 or more values were successfully loaded from the config file.
        self.num_configs_loaded_successfully = load_config_file_tuple[2]

