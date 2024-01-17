import cv2

def contour_detect_alt(img):
    # Blur the image
    image = cv2.GaussianBlur(img, (5, 5), 0)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to the image to separate the objects from the background
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find the contours of the objects in the image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours and calculate the area of each object
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300000:
            continue
        if area > max_area:
            max_area = area
            x, y, w, h = cv2.boundingRect(cnt)
    # Draw a bounding box around each object and display the area on the image
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
