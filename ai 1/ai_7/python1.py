import cv2
import numpy as np
img = cv2.imread("avenger.jpg")
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)  

height,width,channel = img.shape

cv2.line(img,(0,0), (width,height), (0,255, 0), 7)
cv2.rectangle(img,(100,100), (200,300), (125,128,0), -1)
cv2.circle(img, (70,100), 45, (255, 255, 255), -10)
cv2.circle(img,(70,100), 25, (230, 100, 120), -10)
cv2.circle(img, (width-70,100), 45, (255, 255, 255), -10)
cv2.circle(img,(width-70,100), 25, (230, 100, 120), -10)
cv2.putText(img, "REVENGE",(width-250,height-60), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0),2  )
red = ([0, 0, 30], [50, 56, 255])
blue = ([30,0, 0], [255, 150, 50])
green = ([0, 30, 0], [100, 255, 100])
white = ([255, 255, 255], [255, 255, 255])
boundaries = [red,blue,green,white]
for (lower, upper) in boundaries:
  lower = np.array(lower, dtype = "uint8")
  upper = np.array(upper, dtype = "uint8")
  mask = cv2.inRange(img, lower, upper)
  output = cv2.bitwise_and(img, img, mask = mask)
  cv2.imshow("Color Detection", output)
  cv2.waitKey(0)
cv2.imshow("img", img)

print(type(img), img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()