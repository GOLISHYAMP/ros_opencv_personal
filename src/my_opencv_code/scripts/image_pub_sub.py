#!/usr/bin/env python3

import rospy
import cv2
# from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()

def image_callback(ros_image):
    print("got an image")
    global bridge
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image,"bgr8")
    except CvBridgeError as e:
        print(e)

    (rows,cols,channels) = cv_image.shape
    print(cv_image.shape)
    if cols > 200 and rows > 200:
        cv2.circle(cv_image, (100,100), 90, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cv_image, "Webcam activated with ROS and openCV!",(10,350),font,1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("image_window",cv_image)
    cv2.waitKey(3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()

def main(args):
    rospy.init_node("image_converter",anonymous=True)
    image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv)
