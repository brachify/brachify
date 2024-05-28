# object to store all the config and default values
from settings import load
from settings.load import DEFAULT_CONFIG_VALUES
#from classes.app import get_app

class Values():

    def createConfigMessageText(self):
        """
        Generates the string that is printed to the pop-up window to notify user of which values
        were successfully loaded from the config.json file, and which use the default values.
        """
        #app = get_app()
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

