import cv2
import numpy as np
avenger = cv2.imread("avenger.jpg")
exercise = cv2.imread("exercise.jpg")
big_avenge = cv2.resize(avenger, (0,0), fx=1, fy=1)
kungfu = cv2.imread("download.jpg")
bigpanda = cv2.resize(kungfu, (0,0), fx=2, fy=2)

blur = cv2.blur(avenger, (10,10))
gausian = cv2.GaussianBlur(avenger, (5,5), 0)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (160,200), 165, 255, -1)
img = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("avengermask", mask)
cv2.imshow("image", img)
# cv2.imshow("Image Avenger", avenger)
# cv2.imshow("IRON", exercise)
# cv2.imshow("man", big_avenge)
# cv2.imshow("panda", bigpanda)
# cv2.imshow("blind", blur)
# cv2.imshow("gausian", gausian)

print(avenger)

print(type(avenger), avenger.shape) #height, width, colors(b-g-r)
cv2.waitKey(0)
cv2.destroyAllWindows()