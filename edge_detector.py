import cv2

def edge_detect(image):
    squares = []
    image = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edgeimage = cv2.Canny(gray, 30, 100, apertureSize=3)
    contours, _hierarchy = cv2.findContours(edgeimage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("轮廓数量：%d" % len(contours))
    return contours




if __name__ == "__main__":
    img = cv2.imread("case/case1.png")
    edge_detect(img)