import dot_detector
import edge_detector
import argparse

#Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument("-w", "--width", type=float, required=True, help="width of the left-most object in the image (in cm)")
args = vars(ap.parse_args())


img = cv2.imread(args["image"])
dot_detector.red_dot_detect(img)
edge_detector.contour_detect(img)
