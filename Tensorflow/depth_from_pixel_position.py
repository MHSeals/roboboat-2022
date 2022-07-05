# Modified https://github.com/IntelRealSense/librealsense/blob/master/wrappers/python/examples/python-tutorial-1-depth.py

# First import the library
import pyrealsense2 as rs

# Define some constants
width = 640
height = 480
fps = 30

iteration_limit = 10

try:
    # Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()

    # Configure streams
    config = rs.config()
    config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)

    # Start streaming
    pipeline.start(config)

    iterations = 0
    while iterations < iteration_limit:
        # This call waits until a new coherent set of frames is available on a device
        # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth:
            continue

        # Grabs the distance of thing in the middle of the frame
        dist_meters = depth.get_distance(width // 2, height // 2)
        dist_inches = dist_meters * 39.3701
        print(f'{dist_meters} meters ({dist_inches} inches) away from {width // 2}, {height // 2}' )

        iterations += 1

    exit(0)

except Exception as e:
    print(e)
    pass
