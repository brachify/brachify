import numpy as np
from pathlib import Path
import pydicom
from classes.logger import log
from classes.dicom.data import DicomData
from classes.mesh.cylinder import BrachyCylinder
from classes.mesh.channel import NeedleChannel
import classes.mesh.helper as helper
from classes.app import get_app

# get default cylinder diameter from config file.  If can't read from dictionary, set to 30.0.
default_settings = get_app().default_settings
DEFAULT_CYLINDER_DIAMETER = default_settings.get("DEFAULT_CYLINDER_DIAMETER", 30.0) 

def get_cylinder_from_dicom(data: DicomData) -> BrachyCylinder: 
    diameter = data.cylinder_diameter
    tip = data.cylinder_tip
    base = data.cylinder_base

    log.debug(f"Cylinder results: \n Diameter: {diameter}\n Tip: {tip}\n Base: {base}")
    return BrachyCylinder(tip=tip, base=base, diameter=diameter)


def is_rp_file(filepath: str) -> bool:
    """Checks if a file is a RTPLAN DICOM file and if it contains the data for needle channels"""
    try:
        dataset = pydicom.read_file(filepath)

        if dataset.Modality != 'RTPLAN': return False

        # finding the contour data
        channels = dataset.ApplicationSetupSequence[0].ChannelSequence
        if len(channels) < 1:
            return False
    except Exception as error_message:
        log.info(f"Error reading RP DICOM file: {filepath} \n{error_message}")
        return False
    else:
        return True


def is_rs_file(filepath: str) -> bool:
    """Checks if a file is a RTSTRUCT DICOM file and if it contains the data to make a cylinder"""
    try:
        dataset = pydicom.read_file(filepath)

        if dataset.Modality != 'RTSTRUCT': return False


    except Exception as error_message:
        log.info(f"Error reading dicom file: {filepath}\n{error_message}")
        return False

    return True


def load_central_axis_varian(data: DicomData, rs_dataset):

    for sequence in rs_dataset.ROIContourSequence:
        if sequence.ReferencedROINumber == data.central_channel_roi:
            central_channel = sequence
            break

    channel_contour_raw = central_channel.ContourSequence[0].ContourData
    points = [channel_contour_raw[i:i + 3] for i in range(0, len(channel_contour_raw), 3)]
    data.central_channel = points

    data.cylinder_tip = np.asarray(data.central_channel[0])
    data.cylinder_base = np.asarray(data.central_channel[-1])
    data.cylinder_diameter = DEFAULT_CYLINDER_DIAMETER  # hardcoded default. user needs to be flagged...
    data.cylinder_direction = data.cylinder_tip - data.cylinder_base   


def remove_collinear_points(points): #unused, left in case it's needed later.

    def is_collinear(p1, p2, p3):
        """Check if three points are collinear"""
        # Create vectors
        v1 = np.array(p2) - np.array(p1)
        v2 = np.array(p3) - np.array(p2)
        if np.all(v1 == v2):
            return True

        # Calculate the dot product
        dot_product = np.dot(v1, v2)

        # Calculate the magnitude of the vectors
        magnitude_vector1 = np.linalg.norm(v1)
        magnitude_vector2 = np.linalg.norm(v2)
        

        # Calculate the cosine of the angle
        cos_angle = dot_product / (magnitude_vector1 * magnitude_vector2)

        # Calculate the angle in radians
        angle_radians = np.arccos(cos_angle)

        # Convert to degrees, if needed
        angle_degrees = np.degrees(angle_radians)

        parallel = angle_degrees < 0.02
        # print(is_close)
        return parallel

    # Handle lists with fewer than 3 points
    if len(points) < 3:
        return points

    filtered_points = [points[0]]
    last_point = points[0]
    for i in range(1, len(points) - 1):
        if not is_collinear(last_point, points[i], points[i + 1]):
            filtered_points.append(points[i])
            last_point = points[i]
    filtered_points.append(points[-1])

    return filtered_points


def load_central_axis_nucletron(data: DicomData, rp_dataset):
    central_channel = None
    # central_channel = rp_dataset.ApplicationSetupSequence[0].ChannelSequence[data.central_channel_roi].BrachyControlPointSequence
    for contoursequence in rp_dataset[0x300f, 0x1000][0].ROIContourSequence:
        if data.central_channel_roi == int(contoursequence.ReferencedROINumber):
            central_channel = contoursequence.ContourSequence[0].ContourData
            break
    if central_channel is None:
        log.info(f"No central channel contour sequence found corresponding to central channel label: {filepath} \n{error_message}")

    
    central_channel_points = [central_channel[i:i+3] for i in range(0, len(central_channel), 3)] 
    data.central_channel = central_channel_points

    data.cylinder_tip = np.asarray(data.central_channel[0])
    data.cylinder_base = np.asarray(data.central_channel[-1])
    data.cylinder_diameter = DEFAULT_CYLINDER_DIAMETER  # hardcoded default. user needs to be flagged...
    data.cylinder_direction = data.cylinder_tip - data.cylinder_base   


def load_channels_varian(data: DicomData, rs_dataset):
    channel_contours = list(filter(lambda sequence: (sequence.ReferencedROINumber in data.channels_rois),
                                    rs_dataset.ROIContourSequence))

    # channel points are a single array dividable by 3
    # so for each channel, take those three points and put them into a small 3 list
    channel_contour_points = []
    for channel in channel_contours:
        points = [[
            channel.ContourSequence[0].ContourData[i],
            channel.ContourSequence[0].ContourData[i + 1],
            channel.ContourSequence[0].ContourData[i + 2]]
            for i in range(0, len(channel.ContourSequence[0].ContourData), 3)
        ]
        channel_contour_points.append(points)
    data.channel_contours = channel_contour_points

    channel_paths = []
    # use the brachy cylinder to offset the points
    # z axis reference, the direction we want the cylinder and needles to go
    z_up = np.array([0, 0, 1])
    base = data.cylinder_base  # transform offset
    cyl_vec = data.cylinder_direction  # rotation offset
    cyl_length = np.linalg.norm(cyl_vec)
    
    # normalized direction from tip to base
    from classes.mesh.cylinder import DEFAULT_LENGTH
    offset_vector = np.array([0, 0, - cyl_length + DEFAULT_LENGTH])

    updated_base = helper.rotate_points(base, cyl_vec, z_up)
    for i, c in enumerate(channel_contour_points):
        new_points = np.array(c)
        new_points = helper.rotate_points(new_points, cyl_vec, z_up)
        new_points = np.array(new_points) - updated_base
        new_points = new_points + offset_vector
        channel_paths.append(list(list(points) for points in new_points))
    data.channel_paths = channel_paths


def load_channels_nucletron(data: DicomData, rp_dataset):

    # Get the xyz values for each needle that isn't the central needle.
    rp_channels = rp_dataset[0x300f, 0x1000][0].ROIContourSequence
    
    # Initialize a list to store the extracted ContourData
    channel_contours = []

    # Iterate over each item in rp_channels
    for channel in rp_channels:
        # Get the ContourNumber for the current channel
        contour_number = int(channel.ReferencedROINumber)
        
        # Check if the contour_number exists in data.channels_rois
        if contour_number in data.channels_rois:
            # Set the Contour Data index to the contour number: this may cause future problems, there may be a more robust method of doing this.
            index = contour_number
            
            # Extract ContourData using the found index
            contour_data = rp_channels[index].ContourSequence[0].ContourData
            contour_data_float = [float(value_str) for value_str in contour_data]

            # Reshape the contour_data into lists of lists with shape (n, 3)
            reshaped_contour_data = [contour_data[i:i+3] for i in range(0, len(contour_data), 3)]

            # Append the extracted ContourData to the list
            channel_contours.append(reshaped_contour_data)
        else:
            # If the contour_number doesn't exist in data.channels_labels, handle it accordingly
            print(f"ContourNumber {contour_number} not found in data.channels_labels")

    
    channel_paths = []
    # use the brachy cylinder to offset the points
    # z axis reference, the direction we want the cylinder and needles to go
    z_up = np.array([0, 0, 1])
    base = data.cylinder_base  # transform offset
    cyl_vec = data.cylinder_direction  # rotation offset
    cyl_length = np.linalg.norm(cyl_vec)
    
    # normalized direction from tip to base
    from classes.mesh.cylinder import DEFAULT_LENGTH
    offset_vector = np.array([0, 0, - cyl_length + DEFAULT_LENGTH])

    updated_base = helper.rotate_points(base, cyl_vec, z_up)
    for i, c in enumerate(channel_contours):
        new_points = np.array(c)
        new_points = helper.rotate_points(new_points, cyl_vec, z_up)
        new_points = np.array(new_points) - updated_base
        new_points = new_points + offset_vector
        channel_paths.append(list(list(points) for points in new_points))
    data.channel_paths = channel_paths


def load_cylinder_contour(data: DicomData, rs_dataset):
    data.cylinder_roi = list(filter(lambda s: ("surface" in s.ROIObservationLabel.lower()),
                                    rs_dataset.RTROIObservationsSequence))[0].ReferencedROINumber
    cylinder_contour = list(filter(lambda s: (s.ReferencedROINumber == data.cylinder_roi),
                                    rs_dataset.ROIContourSequence))[0]

    data.cylinder_contour = [[
        cylinder_contour.ContourSequence[0].ContourData[i],
        cylinder_contour.ContourSequence[0].ContourData[i + 1],
        cylinder_contour.ContourSequence[0].ContourData[i + 2]]
        for i in range(0, len(cylinder_contour.ContourSequence[0].ContourData), 3)]

    # cylinder offsets
    point1 = np.asarray(data.cylinder_contour[0])
    point2 = np.asarray(data.cylinder_contour[-1])
    difference = point2 - point1
    diameter = np.sqrt((difference[0]) ** 2 +
                    (difference[1]) ** 2 + (difference[2]) ** 2)
    data.cylinder_diameter = round(diameter, 1)

    middle_index = int(len(data.cylinder_contour) / 2)

    data.cylinder_tip = data.cylinder_contour[middle_index]
    data.cylinder_base = point1 + (difference / 2)
    data.cylinder_direction = data.cylinder_tip - data.cylinder_base   


def explore_rp_rs(rp_dataset, rs_dataset):
    # Test
    contours = []
    for contour in rs_dataset.ROIContourSequence[0].ContourSequence:
        contours.append(contour.ContourData)
    channel_contour_points_strings = []
    for channel in contours:
        points = [[
            channel[i],
            channel[i + 1],
            channel[i + 2]]
            for i in range(0, len(channel), 3)
        ]
        channel_contour_points_strings.append(points)

    import matplotlib.pyplot as plt
    # import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

    list_of_lists_of_string_points = channel_contour_points_strings

    # Convert string lists to numpy arrays of floats
    list_of_numeric_arrays = []
    for sublist in list_of_lists_of_string_points:
        numeric_sublist = [np.array(point, dtype=float) for point in sublist]
        list_of_numeric_arrays.append(np.array(numeric_sublist))

    # Create a 3D plot
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Colors and markers for each array
    colors = ['r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b']  # red, green, blue
    markers = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']  # circle, triangle, square

    # Plot each array
    for arr, color, marker in zip(list_of_numeric_arrays, colors, markers):
        for point in arr:
            ax.scatter(point[0], point[1], point[2], c=color, marker=marker)

    # Labeling axes
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()
    plt.pause(1)
    return


def load_varian_dicom_data(rp_file: str, rs_file: str) -> DicomData:
    data = DicomData()

    # Channel ROI Numbers
    try:
        # we use the Planning file to get the channel ROI numbers
        rp_dataset = pydicom.read_file(rp_file)
        data.channels_rois = [
            roi.ReferencedROINumber for roi in rp_dataset.ApplicationSetupSequence[0].ChannelSequence]
        data.channels_labels = [
            roi.SourceApplicatorID for roi in rp_dataset.ApplicationSetupSequence[0].ChannelSequence]
        data.channel_numbers = [
            number.ChannelNumber for number in  rp_dataset.ApplicationSetupSequence[0].ChannelSequence
        ]
        data.patient_name = rp_dataset.PatientName.family_name
        data.patient_id = rp_dataset.PatientID
        data.plan_label = rp_dataset.RTPlanLabel
    except Exception as error_message:
        log.error(f"Reading RP Dicom file failed! {rp_file}\n{error_message}")

    #additional info
    try:
        data.approval_status = rp_dataset.ApprovalStatus
    except Exception as error_message:
        log.error("did not find Approval Status")
    try:
        data.operator = rp_dataset.OperatorsName
    except Exception as error_message:
        log.error("did not find Operators Name")
    

    # Central Axis data
    try:
        # CHECK IF A CENTRAL AXIS NEEDLE IS LABELED/USED
        centralaxisrefROINumber = None
        center_index = None
        for i, label in enumerate(data.channels_labels):
            for mylabel in ["Central Axis", "centralaxis"]:
                if mylabel.lower() in label.lower():
                    centralaxisrefROINumber = data.channels_rois[i]
                    center_index = i
                    break
            if centralaxisrefROINumber: 
                log.debug(f"Found central axis at ROI {centralaxisrefROINumber}")
                break
    except Exception as error_message:
        log.error(f"Error locating central axis: {error_message}")    

    # IF THERE'S A CENTRAL AXIS, ADD IT TO DATA AND REMOVE IT FROM THE LIST
    if centralaxisrefROINumber:
        data.central_channel_roi = data.channels_rois[center_index]
        data.channels_labels.pop(center_index)
        data.channels_rois.pop(center_index)

    # Contour Data
    try:
        # We use the RS file to get the Applicator's ROI and contour data
        # We also use it to get the channel ROI data if we have their ROIS
        rs_dataset = pydicom.read_file(rs_file)

        # cylinder from contour
        try:
            if data.central_channel_roi:  # if a central axis channel was found
                load_central_axis_varian(data, rs_dataset)
            else:  # use a surface contour for the cylinder
                load_cylinder_contour(data, rs_dataset)
        except Exception as error_message:
            log.error(f"Loading RS Dicom surface struct or no central axis identified! {rs_file}\n{error_message}")
        
        # channels info
        if data.channels_rois:
            load_channels_varian(data, rs_dataset)
    except Exception as error_message:
        log.error(f"Loading RS Dicom file failed! {rs_file}\n{error_message}")

    log.debug(f"{data.toString()}")
    return data


def load_nucletron_dicom_data(rp_file: str, rs_file: str) -> DicomData:
    data = DicomData()
    # oncentraflag = False
    # if rp_dataset.Manufacturer == "Nucletron":
        # oncentraflag = True
    # Channel ROI Numbers
    try:
        # we use the Planning file to get the channel ROI numbers
        rp_dataset = pydicom.read_file(rp_file)
        data.channels_rois = [int(channel_label.ROINumber) for channel_label in rp_dataset[0x300f,0x1000][0].StructureSetROISequence] 
        data.channels_labels = [
            roi.SourceApplicatorID for roi in rp_dataset.ApplicationSetupSequence[0].ChannelSequence] #not needed?
        try:
            data.channel_numbers = [
                number.ChannelNumber for number in  rp_dataset.ApplicationSetupSequence[0].ChannelSequence
            ]
        except:
            print("Channel Numbers not loaded -- Nucletron")

        data.patient_name = rp_dataset.PatientName.family_name
        data.patient_id = rp_dataset.PatientID
        data.plan_label = rp_dataset.RTPlanLabel
    except Exception as error_message:
        log.error(f"Reading RP Dicom file failed! {rp_file}\n{error_message}")
    
    #additional info
    try:
        data.approval_status = rp_dataset.ApprovalStatus
    except Exception as error_message:
        log.error("did not find Approval Status")
    try:
        data.operator = rp_dataset.OperatorsName
    except Exception as error_message:
        log.error("did not find Operators Name")

    # Central Axis data
    try:
        # CHECK IF A CENTRAL AXIS NEEDLE IS LABELED/USED
        # centralaxisrefROINumber = None
        # center_index = None
        for i, label in enumerate(data.channels_labels):
            try:
                if rp_dataset[0x300f,0x1000][0].StructureSetROISequence[i].ROIName in ["Central Axis"]:
                    data.central_channel_roi = int(rp_dataset[0x300f,0x1000][0].StructureSetROISequence[i].ROINumber)
                    center_index = i
            except:
                pass
            if data.central_channel_roi is not None: 
                log.debug(f"Found central axis at channel {data.central_channel_roi}")
                break


    except Exception as error_message:
        log.error(f"Error locating central axis: {error_message}")    

    # IF THERE'S A CENTRAL AXIS, ADD IT TO DATA AND REMOVE IT FROM THE LIST
    if data.central_channel_roi is not None:
        data.channels_labels.pop(center_index)
        data.channels_rois.pop(center_index)


    # Contour Data
    try:
        # We use the RS file to get the Applicator's ROI and contour data
        # We also use it to get the channel ROI data if we have their ROIS
        rs_dataset = pydicom.read_file(rs_file) #not using, since elekta stores their channels in the rp file. or do they?
        # explore_rp_rs(rp_dataset, rs_dataset)

        # cylinder from contour
        try:
            if data.central_channel_roi is not None:  # if a central axis channel was found
                load_central_axis_nucletron(data, rp_dataset)
            else:  # use a surface contour for the cylinder
                load_cylinder_contour(data, rs_dataset)
        except Exception as error_message:
            log.error(f"Loading RS Dicom surface struct or no central axis identified! {rs_file}\n{error_message}")
        
        # channels info
        if data.channels_rois:
            load_channels_nucletron(data, rp_dataset)
    except Exception as error_message:
        log.error(f"Loading RS Dicom file failed! {rs_file}\n{error_message}")

    log.debug(f"{data.toString()}")
    return data


def read_dicom_folder(folder_path: str):
        """Used to import a folder, check it for relevant dicom files, and set up the app for the data"""
        files = [ p for p in Path(folder_path).glob('**/*.dcm') if p.is_file()]

        log.debug(f"Found {files} in {folder_path}")

        # look for planning file first
        rp_file = None
        for file in files:
            if is_rp_file(file):
                rp_file = file
                break

        if not rp_file:  # if none of the files within the folder are a rp file
            log.info(f"No rs files where found at {folder_path}")

        # looking for the structure file
        rs_file = None
        for file in files:
            if is_rs_file(file):
                rs_file = file
                break

        if not rs_file:
            log.info(f"No rs file was found in {folder_path}")

        # get data from files
        log.debug(f"Planning file is: {rp_file}")
        log.debug(f"Structure file is: {rs_file}")

        # Determine the TPS
        rp_dataset = pydicom.read_file(rp_file)
        manufacturer = rp_dataset.Manufacturer
        if manufacturer == "Varian Medical Systems":
            data = load_varian_dicom_data(rp_file, rs_file)
        if manufacturer == "Nucletron":
            data = load_nucletron_dicom_data(rp_file, rs_file)
        else:
            pass

        return data
