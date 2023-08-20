import numpy as np
import cv2

cap = cv2.VideoCapture("tennisball.mp4")
desired_width = 800
desired_height = 500
while True:
    ret , image = cap.read()
    # image = cv2.imread("tennisball_04.jpg")
    # image = cv2.imread(Frame)
    image = cv2.resize(image, (desired_width, desired_height))

    cv2.imshow("Original image",image)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV image",hsv)

    yellowlower = (30, 100, 100)
    yellowupper = (60, 255, 255)

    mask = cv2.inRange(hsv, yellowlower, yellowupper)
    cv2.imshow("Masked image",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()