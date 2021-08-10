# Script canny_edge.py is used to watch stream from drone camera and convert it to see edges of an object. It can be used for any other vehicle that uses Robotic Operating System and has camera on it.

import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
import numpy as np


def callback(data):
	br = CvBridge()
	current_frame = br.imgmsg_to_cv2(data)
	edges = cv2.Canny(current_frame, 100, 200)
	cv2.imshow("edges", edges)
	cv2.waitKey(1)
	

def listener():
	rospy.init_node("video_sub_py", anonymous=True)
	rospy.Subscriber('/webcam/image_raw', Image, callback)
	rospy.spin()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
	listener()
