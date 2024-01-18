import cv2
import numpy as np

def show_img(img, winname="image", write_to=None):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    if isinstance(img, str):
        img = cv2.imread(img)
    if write_to:
        cv2.imwrite(write_to, img)
    cv2.imshow(winname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()