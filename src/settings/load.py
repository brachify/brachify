"""
For loading default settings.
"""

from classes.info import DIR_PATH, HOME_PATH, USER_PATH, RESOURCES_PATH
import json
from classes.logger import log


config_values = None

# import the config.json file
def load_config_file():
    # Search in the location where the log is stored to find a config file named "config.json".
    file_name = USER_PATH.joinpath("config.json")
    try:
        # open, read, parse as dictionary, and close the config.json file
        with open(file_name) as json_file:
            json_contents = json.load(json_file)
        # set the default settings to the json dictionary
        config_values = json_contents
        log.debug("successfully loaded default settings from config.json file.")

        config_load_message = []


        # record which keys exist in the config file and which don't
        if "CONFIG_CYLINDER_DIAMETER" in config_values:
            config_load_message.append("\nCONFIG_CYLINDER_DIAMETER is in config_values")
            log.debug("CONFIG_CYLINDER_DIAMETER is in config_values")
        else:
            config_load_message.append("\nCONFIG_CYLINDER_DIAMETER not in config_values")
            log.debug("CONFIG_CYLINDER_DIAMETER not in config_values")


        # creates an attribute to store the message which will be displayed when the main window starts up
        #app.config_load_message = config_load_message
        
        return (config_values, config_load_message)
        
        # create the pop up message
        #app.window.configLoadMessageBox(key_not_found_message)



    
    except:
        # if can't read default settings from config.json file, then use these defaults
        log.debug("Couldn't load settings from config.json file.  Using hard-coded default settings instead.")
    
        config_values = {
            "CONFIG_CYLINDER_DIAMETER": 30.0, 
            "CONFIG_CYLINDER_LENGTH": 160.0, # cylinder length
            "CONFIG_CHANNELS_DIAMETER": 3.0, # channels diameter
            "CONFIG_TANDEM_CHANNEL_DIAMETER": 4.0, 
            "CONFIG_TANDEM_STOPPER_DIAMETER": 8.0, 
            "CONFIG_TANDEM_TIP_ANGLE": 30.0, 
            "CONFIG_TANDEM_TIP_HEIGHT": 129.0, 
            "CONFIG_TANDEM_BEND_RADIUS": 35.0, 
            "CONFIG_NEEDLE_LENGTH": 200.0
        }
    
    return config_values




