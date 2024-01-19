from dot_detector import red_dot_detect
from edge_detector import contour_detect
from edge_detector_alt import contour_detect_alt
import argparse
import cv2
import utils

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = "path to the input image")
ap.add_argument('-w', '--width', type = float, required = True, help = "width between referencing dots in the image (in cm)")
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cm = args['width']

# dot_detector
dot = red_dot_detect(img)
pixel = abs(dot[0][0] - dot[1][0])
ratio = cm / pixel
cv2.line(img, (dot[0][0], dot[0][1]), (dot[1][0], dot[1][1]), color = (0, 255, 0), thickness = 3)
img_alt = img.copy()

# edge_detector
x1, y1, w1, h1 = contour_detect(img)
cv2.putText(img, str(round(w1 * ratio, 2)) + " cm", (x1, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
cv2.putText(img, str(round(h1 * ratio, 2)) + " cm", (x1 + w1 + 20, y1 + h1 // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
utils.show_img(img, "Result", "Result.jpg")

# edge_detector_alt
x2, y2, w2, h2 = contour_detect_alt(img_alt)
cv2.putText(img_alt, str(round(w2 * ratio, 2)) + " cm", (x2, y2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
cv2.putText(img_alt, str(round(h2 * ratio, 2)) + " cm", (x2 + w2 + 20, y2 + h2 // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
utils.show_img(img_alt, "Result_Alt", "Result_Alt.jpg")
