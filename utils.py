import cv2
import numpy as np

def show_img(img):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    if isinstance(img, str):
        img = cv2.imread(img)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()