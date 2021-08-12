import cv2
from cv_bridge import CvBridge
import rospy
from sensor_msgs.msg import Image
import numpy as np


def callback(data):
	br = CvBridge()
	current_frame = br.imgmsg_to_cv2(data)
	gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray, 5)
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=0, maxRadius=0)
	detected_circles = np.uint16(np.around(circles))
	for (x,y,r) in detected_circles[0,:]:
		cv2.circle(current_frame, (x,y), r, (0,255,0), 3)
		cv2.circle(current_frame, (x,y), 2, (0,255,255), 3)
	cv2.imshow("camera", current_frame)
	cv2.waitKey(1)
	

def listener():
	rospy.init_node("video_sub_py", anonymous=True)
	rospy.Subscriber('/webcam/image_raw', Image, callback)
	rospy.spin()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
	listener()
