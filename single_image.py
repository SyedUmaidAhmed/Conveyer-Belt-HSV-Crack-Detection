import cv2

cam = cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)
retval, frame = cam.read()
if retval != True:
    raise ValueError("Can't read frame")

cv2.imwrite('Ahmed.png', frame)
cv2.imshow("img1", frame)
cv2.waitKey(1)
cv2.destroyAllWindows()