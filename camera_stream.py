# Script camera_stream.py is used to watch stream from drone camera. It can be used for any other vehicle that uses Robotic Operating System and has camera on it.

import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
import numpy as np


def callback(data):
	br = CvBridge()
	current_frame = br.imgmsg_to_cv2(data)
	cv2.imshow("camera", current_frame)
	cv2.waitKey(1)
	

def listener():
	rospy.init_node("video_sub_py", anonymous=True)
	rospy.Subscriber('/webcam/image_raw', Image, callback)
	rospy.spin()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
	listener()
