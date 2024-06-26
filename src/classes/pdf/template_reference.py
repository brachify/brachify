from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path 
import subprocess

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image

from classes.dicom.data import DicomData
from classes.logger import log
from classes.mesh.channel import NeedleChannel
from classes.mesh.cylinder import BrachyCylinder
from classes.mesh.tandem import Tandem
from classes.app import get_app

import matplotlib.lines as lines

# BASEMAP = "basemap.png"


def calculate_protrusion_lengths(needles: list, needle_length: float):
    def calculate_cumulative_lengths(needles):
        cumulative_lengths = []

        for needle in needles:
            cumulative_length = 0

            for i in range(1, len(needle)):
                x1, y1, z1 = map(float, needle[i - 1])
                x2, y2, z2 = map(float, needle[i])
                segment_length = ((x2 - x1)**2 + (y2 - y1)
                                  ** 2 + (z2 - z1)**2)**0.5
                cumulative_length += segment_length

            cumulative_lengths.append(cumulative_length)

        return cumulative_lengths
    
    cumulative_lengths = calculate_cumulative_lengths(needles)
    protrusion_lengths = [needle_length - length for length in cumulative_lengths]
    return protrusion_lengths


def index_before_negative_point(channel_list):
    last_index = len(channel_list) - 1
    for i, point in enumerate(channel_list):
        if point[2] < 0:
            return max(0, i - 1)
    return last_index


def extract_points_from_channels(channels: list):
    """
    Retreives the points from NeedleChannels

    Returns:
        [ [x, y, z], [x, y, z], ...]
    """
    channels_list = []
    for channel in channels:
        channel_list = channel.get_points()

        # Filter out points where the z value is less than 0.
        filtered_channel_list = [point for point in channel_list if point[2] > 0]
        
        # Error Checks: We ignore all points below zero (below the bottom of the cylinder)
        # Find the index of the element just before the first instance in channel_list where the third element of the tuple is less than 0
        last_pos_index = index_before_negative_point(filtered_channel_list)

        # Append last point at x,y,0 because channel.get_points() doesn't include the point at the base for some reason.
        final_point = channel_list[last_pos_index][:]
        final_point[2] = 0.0
        channel_list.append(final_point)
        channels_list.append(channel_list)

    return channels_list


def get_all_interstitial_lengths(cylinder: BrachyCylinder, needles: list, spacing: float = 0.1) -> list[float]:
    """
    Example usage:
    needle_interstital_lengths = get_all_interstitial_lengths(needles, base, tip, radius, spacing, CylLen=160)
    Where needles is a list of lists of needle coordinates.
    """

    def generate_cylinder_points(cylinder: BrachyCylinder, spacing: float) -> list[np.array]:
        length = cylinder.length
        base = np.array([0, 0, 0])
        tip = np.array([0, 0, length])
        radius = cylinder.diameter / 2 

        # Step 1: Generate variables
        vec = np.array(tip-base)
        vec_normalized = vec / \
            np.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)
        len_straight = length-radius
        NumStepsStraight = int(np.ceil(len_straight / spacing))
        end_straight_section = base + vec_normalized * len_straight
        CenterLineStraight = np.linspace(
            base, end_straight_section, NumStepsStraight, endpoint=False)
        num_thetas = int(np.ceil(2*np.pi*radius/spacing))
        thetas = np.linspace(0, 2*np.pi, num_thetas, endpoint=False)

        # Step 2: Generate the Straight Part of the Cylinder
        CylinderRing = np.ones((num_thetas, 3))
        CylinderRing[:, 0] = CylinderRing[:, 0] * radius * np.sin(thetas)
        CylinderRing[:, 1] = CylinderRing[:, 1] * radius * np.cos(thetas)
        CylinderStraight = np.ones((NumStepsStraight, num_thetas, 3))
        CylinderStraight[:] = CylinderRing
        CylinderStraight[:, :, 2] = CylinderStraight[:, :, 2]*CenterLineStraight[:, 2, np.newaxis]

        # Step 3: Generate the Dome
        num_phis = int(np.ceil(np.pi/2*radius/spacing))
        phis = np.linspace(0, np.pi/2, num_phis)
        dome_radii = np.cos(phis)*radius

        dome_pts = np.ones((num_phis, num_thetas, 3))
        dome_pts[:, :, 0] = dome_pts[:, :, 0] * \
            np.sin(thetas) * dome_radii[:, np.newaxis]
        dome_pts[:, :, 1] = dome_pts[:, :, 1] * \
            np.cos(thetas) * dome_radii[:, np.newaxis]
        dome_pts[:, :, 2] = dome_pts[:, :, 2] * \
            np.sin(phis)[:, np.newaxis] * radius + len_straight

        # Step 4: Generate the Straight Part Normals
        vec_ring = CylinderRing - base
        # give each of the z component normals a bit of positive slope.
        vec_ring[:, 2] = 0.5
        vec_ring = vec_ring / \
            np.sqrt(np.einsum("ij,ij->i", vec_ring, vec_ring)
                    )[:, np.newaxis]
        vecs = np.ones((NumStepsStraight, num_thetas, 3))
        vecs[:] = vec_ring

        # Step 5: Generate the Dome Normals
        dome_base = end_straight_section
        dome_vecs = dome_pts - dome_base
        dome_vecs_reshaped = np.reshape(
            dome_vecs, (num_phis*num_thetas, 3))
        dome_disps_reshaped_normalized = dome_vecs_reshaped / \
            np.sqrt(np.einsum("ij,ij->i", dome_vecs_reshaped,
                    dome_vecs_reshaped))[:, np.newaxis]
        dome_vecs = np.reshape(
            dome_disps_reshaped_normalized, (num_phis, num_thetas, 3))

        cylinder_points = np.append(CylinderStraight, dome_pts)
        cylinder_points = np.reshape(
            cylinder_points, (NumStepsStraight*num_thetas+num_phis*num_thetas, 3))

        # Fix 1: the way this is made ends up adding a bunch of points 
        # (an amount of num_thetas) and vecs right at the tip of the dome
        # in this fix here we remove them.
        cylinder_points = cylinder_points[0:-num_thetas + 1]

        return cylinder_points

    def get_surface_intersection(surface_cloud, line_points, tol_mm=0.25):
        # Convert the input lists to numpy arrays for efficient calculations
        surface_cloud = np.array(surface_cloud)
        line_points = np.array(line_points)

        # Check if the input arrays have the correct shapes
        if surface_cloud.shape[1] != 3 or line_points.shape[1] != 3:
            raise ValueError("Input arrays must have shape (n, 3)")

        # Calculate the direction vector of the line
        line_displacement = line_points[1] - line_points[0]
        line_displacement = line_displacement.astype(float)
        line_direction = line_displacement/np.linalg.norm(line_displacement)

        # Calculate the vector from one point on the line to each point in the point cloud
        vector_to_points = surface_cloud - line_points[0]

        # Project the vectors onto the line direction
        projection_onto_line = np.dot(vector_to_points, line_direction)

        # Calculate the closest points on the line to each point in the cloud
        closest_points_on_line = line_points[0] + \
            projection_onto_line[:, np.newaxis] * line_direction

        # Check if the closest points are within the bounds of the line segment
        within_line_segment_bounds = np.logical_and(
            0 <= projection_onto_line, projection_onto_line <= np.linalg.norm(line_displacement))

        # Filter out points that are not within the line segment bounds
        closest_points_on_line = closest_points_on_line[within_line_segment_bounds]

        if len(closest_points_on_line) == 0:
            # If no points are within the line segment bounds, return None
            return None

        # Calculate the distance between each point in the cloud and its closest point on the line
        distances = np.linalg.norm(
            surface_cloud[within_line_segment_bounds] - closest_points_on_line, axis=1)

        if np.min(distances) > tol_mm:
            return None

        # Find the index of the point with the minimum distance
        min_distance_index = np.argmin(distances)

        # Return the point on the line and the corresponding point on the surface cloud
        return closest_points_on_line[min_distance_index], surface_cloud[within_line_segment_bounds][min_distance_index]

    def get_interstitial_length(cylinder_points, linepoints):
        # Example Usage
        # length = get_interstitial_length(cylinder_points, linepoints)

        # Get the result from get_surface_intersection
        result = get_surface_intersection(cylinder_points, linepoints)
        if result != None:
            # Calculate the interstitial length based on the intersection point of the line segment with the surface.
            exit_point = result[0]
            end_point = linepoints[1]
            disp = end_point - exit_point
            length = np.linalg.norm(disp)
        else:
            length = 0
        return length

    cylinder_cloud = generate_cylinder_points(cylinder=cylinder, spacing=spacing)
    needle_interstitial_lengths = []

    for needle in needles:
        needle = np.array(needle)
        first_line_segment = np.vstack([needle[1], needle[0]])
        length = get_interstitial_length(cylinder_cloud, first_line_segment)

        if length is not None:
            needle_interstitial_lengths.append(length)
        else:
            needle_interstitial_lengths.append("Error")

    return needle_interstitial_lengths


def get_last_xy_points(needles):
    last_xy_points = []

    for needle in needles:
        # Check if the needle list is not empty and has at least 2 coordinates
        if needle and len(needle[-1]) >= 2:
            # Take only the first two coordinates (x and y)
            last_point = needle[-1][:2]
            last_xy_points.append(last_point)

    return last_xy_points


def process_lengths_and_create_data(is_lengths, protrusion_lengths, label_list, number_list):
    needle_data = []

    for idx, (length_mm, protrusion_length) in enumerate(zip(is_lengths, protrusion_lengths), start=0):
        # Convert lengths from mm to cm and round to one decimal place
        length_cm = round(length_mm / 10, 1)
        protrusion_length_cm = round(protrusion_length / 10, 1)

        # Create a tuple for needle_data with protrusion length in the third column
        needle_info = (
            f"{label_list[idx]}", f"{number_list[idx]}", f"{length_cm} cm", f"{protrusion_length_cm} cm", "")
        needle_data.append(needle_info)

    return needle_data


def save_points_diagram(points: list,
                        number_list: list, 
                        circle_radius: float, 
                        output_filepath: Path, 
                        has_tandem: bool=False, 
                        tandem_rotation: float=0.0,
                        is_tandem_imported: bool=False):
    config = get_app().values.config_values
    channel_diam = config.get("CONFIG_CHANNELS_DIAMETER")
    #tandem will show up at config tandem value even if it is imported
    tandem_diam = config.get("CONFIG_TANDEM_CHANNEL_DIAMETER")

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the circle
    circle = plt.Circle((0, 0), circle_radius, color='black', fill=False, clip_on=False)
    ax.add_artist(circle)

    # include only needles that are within 5cm of the cylinder.
    # (this is left here in case we choose to use it in the future.  Currently, all needles
    # passed to this method are within the cylinder.)
    #gets max x, y value that is within 5cm of cylinders origin for determining plotting
    #area
    #limit refers to the 5cm distance around the perimater of the cylinder where needles are allowed
    limit = 50+circle_radius
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for (x, y) in points:
        if(x>max_x and x <limit):
            max_x=x
        if(y>max_y and y <limit):
            max_y=y
        if(x<min_x and x >-limit):
            min_x=x
        if(y<min_y and x >-limit):
            min_y=y
    
    maxx = max(abs(max_x), abs(min_x))
    maxy = max(abs(max_y), abs(min_y))

    # Set axis limits to fit points inside a square with a border
    ax.set_xlim(min(min_x, -circle_radius), max(max_x, circle_radius))
    ax.set_ylim(min(min_y, -circle_radius), max(max_y, circle_radius))
    #makes frame invisible
    ax.set_frame_on(False)

    # Plot each point as a circle with a number inside or to the right or left if it does not fit inside
    # if channel diameter >= circle_radius/12 there is ~enough room to write numbers inside of channels
    # There could be some distorting of the image if there needles are outside of the cylinder
    if(channel_diam >= circle_radius/12 and maxx<circle_radius and maxy<circle_radius):
        for i, (x, y) in enumerate(points):
            #checks to make sure that needles are within 5 cm of center
            if(((np.sqrt(x**2+y**2))/2)<limit):
                ax.add_artist(plt.Circle((x, -y), channel_diam/2, color='black', fill=False, clip_on=False))
                ax.text(x, -y, str(number_list[i]), color='black', ha='center', va='center')
    else:
        for i, (x, y) in enumerate(points):
            #checks to make sure that needles are within 5 cm of center
            if((np.sqrt(x**2+y**2)/2)<limit):
                ax.add_artist(plt.Circle((x, -y), channel_diam/2, color='black', fill=False, clip_on=False))
                #so that text will print outside of needle channel to the right if the channel is too thin
                if(x<0):
                    ax.text(x-(channel_diam/2), -y, str(number_list[i]), color='black', ha='right', va='center')
                else:
                    ax.text(x+(channel_diam/2), -y, str(number_list[i]), color='black', ha='left', va='center')

    if has_tandem:
        tandem_channel_number = get_app().window.channelsmodel.get_tandem_channel().channel_number
        if(tandem_diam >= circle_radius/12 and maxx<circle_radius and maxy<circle_radius):
            ax.add_artist(plt.Circle((0.0, 0.0), tandem_diam/2, color='black', fill=False))
            ax.text(0.0, 0.0, f'{tandem_channel_number}T', color='black', ha='center', va='center')
        else:
            ax.add_artist(plt.Circle((0.0, 0.0), tandem_diam/2, color='black', fill=False))
            ax.text((channel_diam/2), 0.0, f'{tandem_channel_number}T', color='black', ha='left', va='center')

        # if the tandem was generated, then display a dotted line on the pdf.
        if not is_tandem_imported:
            # add dotted line to indicate tandem direction.
            angle = tandem_rotation
            # construct a line segment of a fixed length, with the angle of rotation of the tandem
            line_length = circle_radius / 2
            end_pt_x = line_length * np.cos(np.radians(angle))
            # must make y-value negative bc the view is from the bottom of the cylinder, with  y-axis pointing down.
            # ie: o ---> x
            #     |
            #     y
            end_pt_y = -1* line_length * np.sin(np.radians(angle)) 
            x_values = [0, end_pt_x]
            y_values = [0, end_pt_y]
            # Line goes from (0,0) to (end_pt_x, end_pt_y)
            ax.add_artist(lines.Line2D(x_values, y_values,color='grey', linestyle='--'))

    # Add a filled black rectangle at the top center of the big circle
    tick_width = 0.2
    tick_height = 1.0
    tick_color = 'black'
    tick_vert_offset = 0.5
    # add the notch
    rect = plt.Rectangle((-tick_width / 2, circle_radius - tick_vert_offset -
                            tick_height), tick_width, tick_height, color=tick_color, fill=True)
    ax.add_artist(rect)

    # Remove axis markers and numbering
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Set axis aspect ratio to be equal
    ax.set_aspect('equal', adjustable='box')

    # Set the Basemap Filepath
    png_path = output_filepath.joinpath('basemap.png')
    # Save the plot as a PNG file
    fig = plt.figure(1, dpi =1000000, clip_on=False)
    fig.savefig(png_path, format='png')
    plt.close()
    return png_path

def channels_inside_cylinder(channels: list[NeedleChannel], diameter: float):
    """
    Returns the channels which go through the bottom of the cylinder.
    """
    radius = diameter / 2
    needles = extract_points_from_channels(channels)
    last_xy_points = get_last_xy_points(needles)
    channels_inside = []
    # if the last point of the channel is within the cylinder radius,
    # then keep that channel.
    for idx, point in enumerate(last_xy_points):
        if np.sqrt(point[0]**2 + point[1]**2) <= radius:
            channels_inside.append(channels[idx])

    return channels_inside

#######################################################
# pdf generation
#######################################################
def generate_pdf(
        dicom: DicomData, 
        cylinder: BrachyCylinder,
        channels: list[NeedleChannel],
        filepath: Path,
        needle_length: float,
        has_tandem: bool, 
        tandem_rotation: float, 
        is_tandem_imported: bool):

    app = get_app()

    # Get today's date in the format "Month Day, Year"
    today_date = datetime.today().strftime('%B %d, %Y')

    # Header information
    header_info = "Patient Specific Cylindrical Template Reference Sheet"
    patient_name = dicom.patient_name
    patient_id = dicom.patient_id
    plan_label = dicom.plan_label or "N/A"

    # Create a PDF document
    pdf = SimpleDocTemplate(str(filepath), pagesize=letter)

    # Content elements for the PDF
    content = []

    # Add header information
    header_style = ParagraphStyle(
        'Header1',
        parent=getSampleStyleSheet()['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,  # Hardcoded font size in points
        alignment=1,  # 0=Left, 1=Center, 2=Right
    )

    header_text = "<u>{}</u>".format(header_info)
    content.append(Paragraph(header_text, header_style))

    # Center alignment for the following paragraphs
    centered_style = getSampleStyleSheet()['Normal']
    centered_style.alignment = 1  # 0=Left, 1=Center, 2=Right

    left_style = getSampleStyleSheet()['Normal']
    left_style.alignment = 0  # 0=Left, 1=Center, 2=Right

    content.append(Paragraph(f"Date: {today_date}", left_style))
    content.append(Paragraph(f"Patient Name: {patient_name}", left_style))
    content.append(Paragraph(f"Patient ID: {patient_id}", left_style))
    content.append(
        Paragraph(f"Plan Label: {plan_label} <br/> <br/>", left_style))
    content.append(Paragraph("<br/>", centered_style))

    # Add table with needle data
    # use only the channels that are inside the cylinder
    diameter = cylinder.diameter
    channels_inside = channels_inside_cylinder(channels, diameter)
    needles_inside = extract_points_from_channels(channels_inside)

    interstitial_lengths = get_all_interstitial_lengths(
        cylinder=cylinder,
        needles=needles_inside)
    
    protrusion_lengths = calculate_protrusion_lengths(needles_inside, needle_length)
    # TODO: Add needle label and channel number instead of "Needle 1" etc.
    #length_label = "Protruding Length for " + str(needle_length) + "mm needle"
    data = [["Name","Channel Number", "Extension (Interstitial Length)", "Protrusion from Base", "Protrusion (measured)"]]

    label_list = [channel.label for channel in channels_inside]
    number_list = [channel.channel_number for channel in channels_inside]
    for label, channel_number, interstitial_length, protruding_length, blank \
    in process_lengths_and_create_data(interstitial_lengths, protrusion_lengths, label_list, number_list):
        data.append([label, channel_number, interstitial_length, protruding_length, blank])

    if has_tandem:
        tandem_label = app.window.dicommodel.data.tandem_channel
        tandem_channel_number = app.window.channelsmodel.get_tandem_channel().channel_number
        data.append([tandem_label, tandem_channel_number, "N/A", "N/A", ""])

    table = Table(data)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(table_style)
    content.append(table)

    # Add the image to the PDF
    # Adjust width and height as needed
    pdf_output_dir = filepath.parent
    circle_radius = cylinder.diameter / 2
    last_xy_points = get_last_xy_points(needles_inside) 
    
    png_path = save_points_diagram(last_xy_points, number_list, circle_radius, pdf_output_dir, has_tandem=has_tandem,
                                    tandem_rotation=tandem_rotation, is_tandem_imported=is_tandem_imported)

    #leaves margin of 25 pixels
    img = Image(str(png_path))
    content.append(img)

    # Build and save the PDF document
    pdf.build(content)

    # Open the generated PDF using the default PDF viewer
    try:
        import os
        if os.name == 'nt':  # Check if on Windows
            try:
                # try opening the pdf using os.startfile
                os.startfile(str(filepath))
                #subprocess.Popen(['start', str(filepath)], shell=False)
            except:
                # if os.startfile throws and exception, then try opening the pdf with subprocess.Popen
                subprocess.Popen(['start', str(filepath)], shell=True)
        elif os.name == 'posix':  # Check if on macOS/Linux
            subprocess.Popen(['open', str(filepath)])
    except Exception as e:
        print(f"Unable to open the PDF: {e}")

    log.info('wait')
