import cv2
import numpy as np
import utils

def red_dot_detect(img):
    img_hsv = cv2.GaussianBlur(img, (5,5), 0)
    img_hsv = cv2.cvtColor(img_hsv, cv2.COLOR_BGR2HSV)
    # First blur to reduce noise prior to color space conversion

    img_hsv_red = cv2.bitwise_or(
        cv2.inRange(img_hsv, np.array([0, 70, 50]), np.array([10, 255, 255])),
        cv2.inRange(img_hsv, np.array([156, 70, 50]), np.array([180, 255, 255])))
    # Second blur to reduce more noise, easier circle detection
    img_hsv_red = cv2.GaussianBlur(img_hsv_red, (5, 5), 2, 2)
    # Use the Hough transform to detect circles in the image
    param2 = 50
    circles = [[]]
    while len(circles[0])<2:
        circles = cv2.HoughCircles(img_hsv_red, cv2.HOUGH_GRADIENT, 1,
            img_hsv_red.shape[0]/8, param1=100, param2=20, minRadius=4, maxRadius=60)
        param2 -=1
        if param2<=0:
            return np.array([[]])
    circles = np.round(circles[0, :]).astype("int")
    print(f"Circles: \n{circles}")
    for c in circles:
        cv2.circle(img, center=(c[0], c[1]), radius=c[2], color=(0, 255, 255), thickness=2)
    #utils.show_img(img)
    return circles

if __name__ == "__main__":
    img = cv2.imread("case/case3.jpg")
    red_dot_detect(img)