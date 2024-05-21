"""
For loading default settings.
"""

from classes.info import DIR_PATH, HOME_PATH, USER_PATH, RESOURCES_PATH
import json
from classes.logger import log

default_settings = None

# import the config.json file
def load_config_file():
    # Search in the location where the log is stored to find a config file named "config.json".
    file_name = USER_PATH.joinpath("config.json")
    try:
        # open, read, parse as dictionary, and close the config.json file
        with open(file_name) as json_file:
            json_contents = json.load(json_file)
        # set the default settings to the json dictionary
        default_settings = json_contents
        log.debug("successfully loaded default settings from config.json file.")
    
    except:
        # if can't read default settings from config.json file, then use these defaults
        log.debug("Couldn't load settings from config.json file.  Using hard-coded default settings instead.")
    
        default_settings = {
            "DEFAULT_CYLINDER_DIAMETER": 30.0, 
            "DEFAULT_LENGTH": 160.0, # cylinder length
            "DEFAULT_DIAMETER": 3.0, # channels diameter
            "TANDEM_CHANNEL_DIAMETER_DEFAULT": 4.0, 
            "TANDEM_STOPPER_DIAMETER_DEFAULT": 8.0, 
            "TANDEM_TIP_ANGLE_DEFAULT": 30.0, 
            "TANDEM_TIP_HEIGHT_DEFAULT": 129.0, 
            "TANDEM_BEND_RADIUS": 35.0, 
            "DEFAULT_NEEDLE_LENGTH": 20
        }
    
    return default_settings




