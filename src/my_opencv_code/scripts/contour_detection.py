import numpy as np
import cv2

def read_rgb_image(image_name, show):
    rgb_image = cv2.imread(image_name)
    rgb_image = cv2.resize(rgb_image,(800,500))
    if show:
        cv2.imshow("RGB image",rgb_image)
    return rgb_image

def convert_rgb_to_gray(rgb_image, show):
    gray_image = cv2.cvtColor(rgb_image,cv2.COLOR_BGR2GRAY)
    gray_image = cv2.resize(gray_image,(800,500))
    if show:
        cv2.imshow("GRAY image",gray_image)
    return gray_image

def convert_gray_to_binary(gray_image, adaptive, show):
    if adaptive:
        binary_image = cv2.adaptiveThreshold(gray_image,
                                             255,
                                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY, 5,2)
    else:
        _,binary_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_BINARY)
    if show:
        cv2.imshow("Binary Image",binary_image)
    return binary_image

def getContours(binary_image):
    contours, hierarchy = cv2.findContours(binary_image,
                                              cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours, image_name):
    index = -1
    thickness = 2
    color = (255,0,255)
    cv2.drawContours(image, contours, index, color, thickness)
    cv2.imshow(image_name, image)

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx = -1
    cy = -1
    if (M["m00"]!=0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    return cx,cy

def process_contours (binary_image, rgb_image, contours): 
    # black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3],)
    for c in contours:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if area > 100:
            cv2.drawContours(rgb_image, [c], -1, (150,250,150),1)
            # cv2.drawContours (black_image, (c), -1, (150,250,150), 1)
            cx, cy =  get_contour_center(c)
            cv2.circle(rgb_image, (cx,cy), (int)(radius), (0,0,255),1)
            # cv2.circle(black_image, (cx, cy), (int) (radius), 
        print ("Area: {}, Perimeter: {}".format(area, perimeter))
        print("number of contours: {}".format(len(contours)))
        cv2.imshow("RGB Image Contours", rgb_image) 
        # cv2.imshow("Black Image Contours", black image)



def main():
    image_name = "shapes.jpg"
    rgb_image = read_rgb_image(image_name, True)
    gray_image = convert_rgb_to_gray(rgb_image,True)
    binary_image = convert_gray_to_binary(gray_image,True, True)
    contours = getContours(binary_image)
    # draw_contours(rgb_image, contours, "RGB Contours")
    process_contours(binary_image, rgb_image, contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()