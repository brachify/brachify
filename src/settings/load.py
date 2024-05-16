"""
For loading default settings.
"""

from classes.info import DIR_PATH, HOME_PATH, USER_PATH, RESOURCES_PATH
import json
from classes.logger import log

print("DIR_PATH: ", DIR_PATH) # DIR_PATH:  c:\Users\stephanie.merkl\Documents\Python\brachify\src\classes
print("HOME_PATH: ", HOME_PATH) # HOME_PATH:  C:\Users\stephanie.merkl
print("USER_PATH: ", USER_PATH) # USER_PATH:  C:\Users\stephanie.merkl\brachify
print("RESOURCES_PATH: ", RESOURCES_PATH) # RESOURCES_PATH:  c:\Users\stephanie.merkl\Documents\Python\brachify\src\classes\resources

# For now I will use "USER_PATH" for the location of the config file, as that is where the log is stored
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
        "DEFAULT_CYLINDER_DIAMETER": 30.1, 
        "DEFAULT_LENGTH": 161.0, # cylinder length
        "DEFAULT_DIAMETER": 3.1, # channels diameter
        "TANDEM_CHANNEL_DIAMETER_DEFAULT": 4.1, 
        "TANDEM_STOPPER_DIAMETER_DEFAULT": 8.1, 
        "TANDEM_TIP_ANGLE_DEFAULT": 30.1, 
        "TANDEM_TIP_HEIGHT_DEFAULT": 129.1, # Doesn't seem to work. XX
        "TANDEM_BEND_RADIUS": 35.1, 
        "DEFAULT_NEEDLE_LENGTH": 201
    }


