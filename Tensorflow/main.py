# Modified https://github.com/IntelRealSense/librealsense/blob/master/wrappers/python/examples/python-tutorial-1-depth.py

# First import the library
import pyrealsense2 as rs
import numpy as np
import cv2
import tensorflow as tf
import tensorflow.lite
from tflite_support.task import vision
from tflite_support.task import core
from tflite_support.task import processor

base_options = core.BaseOptions(file_name="./model.tflite", num_threads=2)
detection_options = processor.DetectionOptions(max_results=1, score_threshold=.5)
options = vision.ObjectDetectorOptions(base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)


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
    config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
    # Start streaming
    pipeline.start(config)
    iterations = 0
    while True:
        # This call waits until a new coherent set of frames is available on a device
        # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        color = frames.get_color_frame()
        color_image = np.asanyarray(color.get_data())
        if not depth:
            continue
        image = vision.TensorImage.create_from_array(color_image)
        detection_result = detector.detect(image)
        if len(detection_result.detections) != 0:
            x_orig = detection_result.detections[0].bounding_box.origin_x
            y_orig = detection_result.detections[0].bounding_box.origin_y
            width = detection_result.detections[0].bounding_box.width
            height = detection_result.detections[0].bounding_box.height
            name = detection_result.detections[0].categories[0].category_name

            x_center = x_orig + int(width/2)
            y_center = y_orig + int(height/2)

            # Grabs the distance of thing in the middle of the frame
            dist_meters = depth.get_distance(x_center, y_center)
            print(str(dist_meters) + " meters away from " + name + " at position "  + str(x_center) + "," + str(y_center))

        iterations += 1

    exit(0)

except Exception as e:
    print(e)
    pass
