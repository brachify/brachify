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
    
    except:
        # if can't read default settings from config.json file, then use these defaults
        log.debug("Couldn't load settings from config.json file.  Using hard-coded default settings instead.")
    
        config_values = {
            "CONFIG_CYLINDER_DIAMETER": 30.0, 
            "CONFIG_LENGTH": 160.0, # cylinder length
            "CONFIG_DIAMETER": 3.0, # channels diameter
            "CONFIG_TANDEM_CHANNEL_DIAMETER": 4.0, 
            "CONFIG_TANDEM_STOPPER_DIAMETER": 8.0, 
            "CONFIG_TANDEM_TIP_ANGLE": 30.0, 
            "CONFIG_TANDEM_TIP_HEIGHT": 129.0, 
            "CONFIG_TANDEM_BEND_RADIUS": 35.0, 
            "CONFIG_NEEDLE_LENGTH": 20
        }
    
    return config_values




