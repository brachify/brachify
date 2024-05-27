"""
For loading default settings.
"""

from classes.info import USER_PATH
import json
from classes.logger import log


config_values = None

# import the config.json file
def load_config_file():
    # Search in the location where the log is stored to find a config file named "config.json".
    file_name = USER_PATH.joinpath("config.json")

    # a list containing 2 lists:
    # [0] contains a list of all the keys/values that were successfully loaded from the config file
    # [1] contains a list of all the keys that did not exist in the config file
    config_load_message = [[],[]]

    try:
        # open, read, parse as dictionary, and close the config.json file
        with open(file_name) as json_file:
            json_contents = json.load(json_file)
        # set the default settings to the json dictionary
        config_values = json_contents
        log.debug("Successfully loaded a config.json file.")

        # check which keys exist in the loaded file, and compile a list of which exist and which don't
        checkValuesExist(config_values, config_load_message)

        return (config_values, config_load_message)
            
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

        config_load_message[1] = [key for key in config_values]

        return (config_values, config_load_message)
    


def checkValuesExist(config_values: dict, config_load_message: list):
    # record which keys exist in the config file and which don't

    desiredAttributes = [
        "CONFIG_CYLINDER_DIAMETER",
        "CONFIG_CYLINDER_LENGTH",
        "CONFIG_CHANNELS_DIAMETER",
        "CONFIG_TANDEM_CHANNEL_DIAMETER",
        "CONFIG_TANDEM_STOPPER_DIAMETER", 
        "CONFIG_TANDEM_TIP_ANGLE",
        "CONFIG_TANDEM_TIP_HEIGHT",
        "CONFIG_TANDEM_BEND_RADIUS",
        "CONFIG_NEEDLE_LENGTH"
    ]

    for elem in desiredAttributes:
        if elem in config_values:
            config_load_message[0].append(f"\n{elem}")
            log.debug(f"{elem} is in config_values")
        else:
            config_load_message[1].append(f"\n{elem}")
            log.debug(f"{elem} not in config_values")


