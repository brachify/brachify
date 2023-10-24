import sys
sys.path.append(f"C://Users//nsmel//Documents//Programming//python//brachify")
import Application.BRep.Channel as channel
import Application.BRep.Helper as helper
import OCC.Core.gp as gp
from OCC.Core.TopoDS import TopoDS_Shape

CHANNEL1 =  [[8.07, -0.78, 101.22], [6.22, 38.91, 39.66], [6.18, 39.48, 38.6], [6.13, 40.05, 37.43], [6.08, 40.63, 36.16], [6.03, 41.0, 34.99], [5.98, 41.48, 33.71], [5.92, 41.76, 32.43], [5.86, 42.04, 31.15], [5.8, 42.23, 29.86], [5.73, 42.31, 28.56], [4.21, 44.17, -1.34], [3.6, 47.89, -37.78]]
CHANNEL2 =  [[4.12, 56.85, 72.98], [4.31, 53.0, 32.79], [4.31, 52.83, 32.08], [4.31, 52.66, 31.47], [4.31, 52.59, 30.86], [4.31, 52.53, 30.16], [4.31, 52.46, 29.55], [4.31, 52.4, 28.85], [4.31, 52.43, 28.25], [4.31, 52.36, 27.55], [4.31, 52.4, 26.95], [4.31, 52.43, 26.25], [4.3, 53.97, -3.71]]
CHANNEL3 =  [[-8.26, 53.11, 76.54], [-3.28, 49.8, 36.34], [-3.2, 49.65, 35.63], [-3.11, 49.5, 35.03], [-3.07, 49.44, 34.42], [-3.04, 49.37, 33.72], [-3.01, 49.31, 33.12], [-2.98, 49.24, 32.41], [-3.0, 49.26, 31.81], [-2.97, 49.2, 31.11], [-3.0, 49.21, 30.51], [-3.02, 49.23, 29.81], [-4.14, 50.07, -0.16]]
CHANNEL4 =  [[13.99, 52.27, 75.1], [14.29, 49.11, 31.09], [14.28, 48.96, 30.38], [14.28, 48.8, 29.77], [14.28, 48.74, 29.16], [14.28, 48.69, 28.46], [14.28, 48.63, 27.85], [14.28, 48.58, 27.15], [14.28, 48.62, 26.55], [14.28, 48.57, 25.84], [14.28, 48.61, 25.25], [14.28, 48.65, 24.55], [14.27, 50.68, -5.38]]
CHANNEL5 =  [[8.61, 16.48, 63.69], [6.74, 32.95, 13.93], [6.71, 33.23, 13.26], [6.68, 33.49, 12.69], [6.65, 33.66, 12.1], [6.61, 33.84, 11.42], [6.59, 34.0, 10.83], [6.55, 34.18, 10.15], [6.52, 34.25, 9.55], [6.49, 34.43, 8.87], [6.45, 34.5, 8.28], [6.42, 34.57, 7.58], [4.87, 37.94, -22.19]]
CHANNEL6 =  [[-5.77, 20.56, 68.17], [-1.98, 36.11, 14.42], [-1.84, 36.32, 13.74], [-1.69, 36.51, 13.15], [-1.62, 36.65, 12.56], [-1.56, 36.79, 11.87], [-1.49, 36.93, 11.29], [-1.42, 37.07, 10.6], [-1.43, 37.14, 10.0], [-1.37, 37.29, 9.31], [-1.38, 37.36, 8.72], [-1.39, 37.45, 8.02], [-1.94, 41.06, -21.75]]
CHANNEL7 =  [[21.73, 31.54, 70.44], [14.5, 37.49, 14.1], [14.31, 37.68, 13.42], [14.12, 37.86, 12.85], [14.0, 37.98, 12.26], [13.88, 38.1, 11.58], [13.77, 38.21, 10.99], [13.65, 38.34, 10.3], [13.61, 38.38, 9.71], [13.48, 38.51, 9.02], [13.45, 38.56, 8.43], [13.4, 38.61, 7.73], [11.42, 41.08, -22.1]]
points = [CHANNEL1, CHANNEL2, CHANNEL3, CHANNEL4, CHANNEL5, CHANNEL6, CHANNEL7]


def task():
    """
    Test the time it takes to make needle channel shapes
    """
    for i in range(len(points)):
       channel_shape = channel.rounded_channel(points[i])


def without_fused():
    """
    Making needle channel shapes without fusing them
    """
    for i in range(len(points)):
       channel_shape = without_fused_channel(points[i])

def without_fused_channel(channel_points, offset: float = 0.0, diameter: float = 3.0) -> TopoDS_Shape:
    """
    If a needle channel has a long distance between the first and second point, this helps stub it
    """
    NEEDLE_LENGTH = 2.50

    if len(channel_points) < 3:
        print(F"Needle Channel Generation error! needs 3 or more points!")
        return None

        # offset points using z axis and cylinder's offset
        # and convert into a gp_Pnt
    points = []
    for point in channel_points:
        points.append(gp.gp_Pnt(point[0], point[1], point[2] - offset))

    radius = diameter / 2
    pipe = []
    # generate starting point on top (cone)
    p1 = points[0]
    p2 = points[1]
    length = helper.get_magnitude(p1, p2)
    if length < NEEDLE_LENGTH:
        pipe.append(channel._cone_pipe(p1, p2, radius))
    else:
        vector = helper.get_vector(p1, p2, length=NEEDLE_LENGTH)
        p_mid = gp.gp_Pnt(p1.X() + vector.X(), p1.Y() +
                       vector.Y(), p1.Z() + vector.Z())
        cone = channel._cone_pipe(p1, p_mid, radius)
        pipe.append(channel._rounded_pipe(p_mid, p2, radius))

    # rest of the points
    for i in range(1, len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        pipe.append(channel._rounded_pipe(p1, p2, radius))

    # curve downwards
    curve = channel._curved_end(points, radius)
    pipe.append(curve)
    return pipe


if __name__ == '__main__':
    import timeit
    print(f"Testing Needle Channels script: Application.BRep.Channel")
    count = 10

    # normal function
    result = timeit.timeit('task()', setup='from __main__ import task', number = count)
    print(f"Shaping 7 channels for {count} times took: {result:.3f} seconds")

    # fuseless function
    result = timeit.timeit('without_fused()', setup='from __main__ import without_fused', number = count)
    print(f"without_fused(): {count} times took: {result:.3f} seconds")
    input("Press any key to continue...")