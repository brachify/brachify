"""
For loading default settings.
"""

from classes.info import DIR_PATH, HOME_PATH, USER_PATH, RESOURCES_PATH
import json
from classes.logger import log
from classes.app import get_app

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


def resetAllValues(values_dict: dict):
    """
    Resets all values in spin boxes to the values in the given dictionary and applies them to the views.
    """
    ###############################
    # Will need to change this function later after config-load-pop-up PR is merged to main.
    # Move this function to be a function of the Values class, so will have to accept self as an arg.
    ###############################
    
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


    


