from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.TopoDS import TopoDS_Shape
from PyQt5.QtWidgets import QListWidgetItem
from Application.BRep.channel import generate_curved_channel
from Presentation.MainWindow.core import MainWindow
import Presentation.Features.NeedleChannels.NeedlesDisplay as needlesDisplay
from Presentation.Features.NeedleChannels.needlesModel import NeedlesModel
from Core.Models.NeedleChannel import NeedleChannel

import numpy as np

'''
Manages the functions and display values for the Needles and the Channel View
self.display_needles: all needle channels fused as a single model
self.display_needle_list: a list of the needle channels
self.needles_active_index: the current active needle channel
'''


def setActiveNeedleChannel(window: MainWindow, index: int = -1) -> None:
    if window.needles_active_index == index:
        return

    window.needles_active_index = index
    if len(window.ui.channelsListWidget.selectedIndexes()) < 1 or \
            index != window.ui.channelsListWidget.selectedIndexes()[0].row():
        window.ui.channelsListWidget.setCurrentRow(index)
    needlesDisplay.view(window)


def setCylinderVisibility(window: MainWindow) -> None:
    window.isCylinderHidden = window.ui.checkBox_hide_cylinder.isChecked()
    needlesDisplay.view(window)


def get_clicked_needle_index(window: MainWindow, shape) -> int:
    for i, needle in enumerate(window.display_needles_list):
        if shape == needle:
            return i

    return -1


def setChannelOffset(window: MainWindow, offset: int) -> None:
    index = window.needles_active_index
    if index < 0:
        return

    old_value = window.ui.slider_needle_extension.value()
    # if old_value != offset:
    #     window.ui.slider_needle_extension.setValue(offset)

    channel = window.needles.channels[window.needles_active_index]
    channel.curve_downwards = offset

    reshape(window, channel)


def setNeedleDisabled(window: MainWindow):
    index = window.needles_active_index
    if index < 0:
        return

    channel = window.needles.channels[window.needles_active_index]
    channel.disabled = not channel.disabled
    recalculate(window)


def recalculate(window: MainWindow):
    '''
    Called after the Needle Channels are changed.
    Generates each channel's shape and saves them in self.display_needles_list
    Then fuses them together and saves that model in self.display_needles
        
    the needles list is used only for channels view
    the fused model is used in all other views and to boolean subtract
    
    also set the tandem offset from the first needle channel
    '''
    print("Recalculating channels!")
    diameter = window.ui.channelDiameterSpinBox.value()
    window.display_needles_list = []
    window.display_needles = None
    for needle in window.needles.channels:
        if needle.disabled:
            continue
        needle.shape = generate_curved_channel(
            channel=needle,
            cylinder_offset=window.ui.cylinderLengthSpinBox.value() - 200.0,
            diameter=window.ui.channelDiameterSpinBox.value())
        window.display_needles_list.append(needle.shape)
        if window.display_needles:
            window.display_needles = BRepAlgoAPI_Fuse(window.display_needles, needle.shape).Shape()
        else:
            window.display_needles = needle.shape

    set_tandem_offsets(window)
    needlesDisplay.view(window)


def reshape(window: MainWindow, channel: NeedleChannel):
    '''
    Needle Channel shapes are saved within the NeedleChannel class
    '''

    print("reshaping channel")
    diameter = window.ui.channelDiameterSpinBox.value()
    cylinder_offset = window.ui.cylinderLengthSpinBox.value() - 200.0
    window.display_needles = None  # can be recalculated later when needed
    if channel.disabled:
        channel.shape = None
    else:
        channel.shape = generate_curved_channel(channel=channel, cylinder_offset=cylinder_offset, diameter=diameter)

    set_tandem_offsets(window)
    needlesDisplay.update(window)


def set_tandem_offsets(window: MainWindow) -> None:
    tandem_channel = window.needles.channels[0]

    # position
    window.tandem_offset_position = tandem_channel.points[-1]

    # rotation
    window.tandem_offset_rotation = tandem_channel.getRotation()
    print(f"Rotation calculated: {window.tandem_offset_rotation}")


def add_rp_file(window: MainWindow, filepath: str) -> None:
    import Application.Imports.import_dicom_planning as dicom_planning
    window.ui.lineedit_dicom_rp.setText(filepath)

    # get data from dicom
    channels = dicom_planning.read_needles_file(filepath)

    # offset each point
    if window.brachyCylinder:
        z_up = np.array([0, 0, 1])  # z axis reference, the direction we want the cylinder and needles to go
        tip = np.array(window.brachyCylinder.tip)
        base = np.array(window.brachyCylinder.base)
        cyl_vec = tip - base  # the cylinder's original vector
        cyl_length = np.linalg.norm(cyl_vec)
        offset_vector = np.array([0, 0, - cyl_length])  # normalized direction from tip to base
        for i, c in enumerate(channels):
            new_points = np.array(c.rawPoints) - base
            new_points = dicom_planning.Rotate_Cloud(new_points, cyl_vec, z_up)
            new_points = new_points - offset_vector
            channels[i].points = list(list(points) for points in new_points)
    window.needles = NeedlesModel(channels=channels)
    for needle in window.needles.channels:
        window.ui.channelsListWidget.addItem(needle.channelId)

    diameter = 3.00

    window.ui.channelDiameterSpinBox.setValue(diameter)
    from Presentation.MainWindow.ui_functions import UIFunctions
    UIFunctions.setPage(window, UIFunctions.NEEDLE_CHANNELS_VIEW)
