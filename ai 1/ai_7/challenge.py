import cv2
import numpy as np

man = cv2.imread("exercise.jpg")
print(type(man), man.shape)

cv2.circle(man, (390, 390), 40, (255, 255, 255), 2)
cv2.rectangle(man, (20, 60), (160, 420), (255,255,255), -1)
text1 = cv2.putText(man, ("This square"), (40, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

cv2.imshow("man", man)

cv2.waitKey(0)
cv2.destroyAllWindows()