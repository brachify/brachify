import numpy as np

def convert_control_point(brachyControlPoint):
    position = brachyControlPoint.ControlPoint3DPosition
    point = [position[0], position[1], position[2]]
    return point

def Rotate_Cloud(Points, V1, V2):
    # V1 is the current vector which the coordinate system is aligned to
    # V2 is the vector we want the system aligned to
    # Points is an (n,3) array of n points (x,y,z)
    V1 = np.asarray(V1)
    V2 = np.asarray(V2)

    # Normalize V1 and V2 in case they aren't already
    V1Len = (V1[0] ** 2 + V1[1] ** 2 + V1[2] ** 2) ** 0.5
    V2Len = (V2[0] ** 2 + V2[1] ** 2 + V2[2] ** 2) ** 0.5
    V1 = V1 / V1Len
    V2 = V2 / V2Len

    # Calculate the vector cross product
    V1V2Cross = np.cross(V1, V2)
    V1V2CrossNorm = (V1V2Cross[0] ** 2 + V1V2Cross[1] ** 2 + V1V2Cross[2] ** 2) ** 0.5
    V1V2CrossNormalized = V1V2Cross / V1V2CrossNorm

    # Dot product
    V1V2Dot = np.dot(V1, V2)
    V1Norm = (V1[0] ** 2 + V1[1] ** 2 + V1[2] ** 2) ** 0.5
    V2Norm = (V2[0] ** 2 + V2[1] ** 2 + V2[2] ** 2) ** 0.5

    # Angle between the vectors
    Theta = np.arccos(V1V2Dot / (V1Norm * V2Norm))

    # Using Rodrigues' rotation formula (wikipedia):
    e = V1V2CrossNormalized

    pts_rotated = np.empty((len(Points), 3))
    if np.size(Points) == 3:
        p = Points
        p_rotated = np.cos(Theta) * p + np.sin(Theta) * (np.cross(e, p)) + (1 - np.cos(Theta)) * np.dot(e, p) * e
        pts_rotated = p_rotated
    else:
        for i, p in enumerate(Points):
            p_rotated = np.cos(Theta) * p + np.sin(Theta) * (np.cross(e, p)) + (1 - np.cos(Theta)) * np.dot(e, p) * e
            pts_rotated[i] = p_rotated
    return pts_rotated