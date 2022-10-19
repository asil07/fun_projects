import cv2
import numpy
cam = cv2.VideoCapture(1)
while cam.isOpened():

    grabbed, frame = cam.read()
    grabbed, frame2 = cam.read()

    diff = cv2.absdiff(frame, frame2)
    # diff = cv2.resize(diff, (900, 600))
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)


    cv2.imshow("Video", frame)

    if cv2.waitKey(10) == ord('q'):
        break








