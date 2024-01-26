import cv2
import numpy as np
import utils
from dot_detector import red_dot_detect


def contour_detect(img):
    image = cv2.GaussianBlur(img, (9, 9), 0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edgeimage = cv2.Canny(gray, 30, 100, apertureSize=3)
    ret, thresh_l = cv2.threshold(gray, 200, 128, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret, thresh_h = cv2.threshold(gray, 200, 128, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(thresh_l.shape)
    mask = np.ones_like(thresh_l)*255
    cv2.rectangle(mask, [int(i*0.2) for i in thresh_l.shape[::-1]], [int(i*0.8) for i in thresh_l.shape[::-1]], color=(0,0,0), thickness=-1)
    edgeimage = cv2.bitwise_or(edgeimage, (
        thresh_l if
        cv2.countNonZero(cv2.bitwise_and(thresh_l,mask)) < cv2.countNonZero(cv2.bitwise_and(thresh_h,mask))
        else thresh_h))

    #utils.show_img(edgeimage)

    contours, _hierarchy = cv2.findContours(edgeimage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    red_dot = red_dot_detect(img)

    dot = []
    for c in contours:
        # 找到边界坐标
        x, y, w, h = cv2.boundingRect(c)  # 计算点集最外面的矩形边界
        for d in red_dot:
            if cv2.pointPolygonTest(
                np.array([[x,y], [x+w, y], [x+w, y+h], [x, y+h]], np.int32).reshape((-1, 1, 2)), (int(d[0]), int(d[1])), False)!=-1:
                    break
        else:dot.append([x, y, w, h])

    # 找出最大矩形的 x,y,w,h,area

    for i in range(1,2):
        x, y, w, h = sorted(dot, key=lambda x: x[2]*x[3])[-i]
        # 在原图上画出最大的矩形
        cv2.rectangle(img, (x, y), (x + w , y + h ), (0, 255, 0), 2)

    #utils.show_img(img)


    """max_contour = approx_polygon(contours)
    img2 = img.copy()
    #cv2.drawContours(img2, contours, -1, (0, 0, 255), 1)
    cv2.drawContours(img2, [max_contour], -1, (0, 0, 255), 1)

    showimg(img2)"""
    return x, y, w, h





if __name__ == "__main__":
    import os
    for i in os.listdir("case"):
        img = cv2.imread(f"case/{i}")
        contour_detect(img)


