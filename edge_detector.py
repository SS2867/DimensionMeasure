import cv2
import numpy as np
import utils


def contour_detect(img):
    image = cv2.GaussianBlur(img, (9, 9), 0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edgeimage = cv2.Canny(gray, 30, 100, apertureSize=3)

    contours, _hierarchy = cv2.findContours(edgeimage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    dot = []
    for c in contours:
        # 找到边界坐标
        x, y, w, h = cv2.boundingRect(c)  # 计算点集最外面的矩形边界
        dot.append([x, y, w, h])

    # 找出最大矩形的 x,y,w,h,area
    x, y, w, h = sorted(dot, key=lambda x: x[2]*x[3])[-1]
    # 在原图上画出最大的矩形
    cv2.rectangle(img, (x, y), (x + w , y + h ), (0, 255, 0), 2)

    #utils.show_img(image)


    """max_contour = approx_polygon(contours)
    img2 = img.copy()
    #cv2.drawContours(img2, contours, -1, (0, 0, 255), 1)
    cv2.drawContours(img2, [max_contour], -1, (0, 0, 255), 1)

    showimg(img2)"""
    return x, y, w, h



"""def approx_polygon(contours):
    contours = approx(contours)
    return sorted(contours, key=lambda x: cv2.contourArea(x))[-1]

def approx(contours):
    squares = []
    for cnt in contours:
        cnt_len = cv2.arcLength(cnt, True) #计算轮廓周长
        con = cv2.approxPolyDP(cnt, 0.02*cnt_len, True) #多边形逼近

        ep = 0.02 * cv2.arcLength(cnt, True)
        con = cv2.approxPolyDP(cnt, ep, True)
        while (1):
            if len(con) <= 4:#防止程序崩溃设置的<=4
                break
            else:
                ep = ep * 1.5
                con = cv2.approxPolyDP(cnt, ep, True)
                continue

        if cv2.contourArea(con) > 0: # and cv2.isContourConvex(cnt):
            squares.append(con)
    return squares"""

if __name__ == "__main__":
    img = cv2.imread("case/case3.jpg")
    contour_detect(img)


