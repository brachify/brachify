"""
For loading default settings.
"""

from classes.info import USER_PATH
import json
from classes.logger import log

DEFAULT_CONFIG_VALUES = {
    "CONFIG_CYLINDER_DIAMETER": 30.0, 
    "CONFIG_CYLINDER_LENGTH": 160.0, # cylinder length
    "CONFIG_CHANNELS_DIAMETER": 3.0, # channels diameter
    "CONFIG_TANDEM_CHANNEL_DIAMETER": 4.0, 
    "CONFIG_TANDEM_STOPPER_DIAMETER": 8.0, 
    "CONFIG_TANDEM_TIP_ANGLE": 30.0, 
    "CONFIG_TANDEM_TIP_HEIGHT": 129.0, 
    "CONFIG_TANDEM_BEND_RADIUS": 35.0, 
    "CONFIG_NEEDLE_LENGTH": 200.0,
    "CONFIG_THREADING": False,
    "CONFIG_THREADING_DEPTH": None,
    "CONFIG_THREADING_RADIUS": None
}
config_values = None

# import the config.json file
def load_config_file():
    # Search in the location where the log is stored to find a config file named "config.json".
    file_name = USER_PATH.joinpath("config.json")

    # a list containing 2 lists:
    # [0] contains a list of all the keys/values that were successfully loaded from the config file
    # [1] contains a list of all the keys that did not exist in the config file
    config_keys_loaded = [[],[]]

    try:
        # open, read, parse as dictionary, and close the config.json file
        with open(file_name) as json_file:
            json_contents = json.load(json_file)
        # set the default settings to the json dictionary
        config_values = json_contents
        log.debug("Successfully loaded a config.json file.")

        # check which keys exist in the loaded file, and compile a list of which exist and which don't.
        checkValuesExist(config_values, config_keys_loaded)

        return (config_values, config_keys_loaded)
            
    except:
        # if can't read default settings from config.json file, then use the defaults.
        log.debug("Couldn't load settings from config.json file.  Using hard-coded default settings instead.")
        config_values = DEFAULT_CONFIG_VALUES
        config_keys_loaded[1] = [key for key in config_values]

        return (config_values, config_keys_loaded)
    


def checkValuesExist(config_values: dict, config_keys_loaded: list):
    # record which keys exist in the config file and which don't.
    for key in DEFAULT_CONFIG_VALUES:
        if (key in config_values) and \
              (isinstance(config_values.get(key), int) or isinstance(config_values.get(key), float)):
            # if the desired key is found in the pre-existing dict, then save that key name in a list.
            # also checks that the value is an int or float (ie a valid format).
            config_keys_loaded[0].append(key)
            log.debug(f"{key} is in config_values")
        else:
            # if the desired key is not found, then save that key name to a different list, and create a key-value for it.
            config_keys_loaded[1].append(key)
            log.debug(f"{key} not in config_values")
            config_values[key] = DEFAULT_CONFIG_VALUES.get(key)
            # Note: the keys in config_values that are not used (ie, they are misnamed), are NOT deleted.
            # they remain, but are simply not used.



