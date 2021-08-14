import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
import numpy as np

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('snimak.avi', fourcc, 20.0, (640,480))

def callback(data):
	br = CvBridge()
	current_frame = br.imgmsg_to_cv2(data)
	out.write(current_frame)
	cv2.imshow("camera", current_frame)
	cv2.waitKey(1)

def listener():
	rospy.init_node("video_sub_py", anonymous=True)
	rospy.Subscriber('/webcam/image_raw', Image, callback)
	rospy.spin()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
	listener()
