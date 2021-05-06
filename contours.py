import cv2 as cv
import numpy as np

img = cv.imread("images/LeBron_James_crop.jpg")
cv.imshow("Lebron James",img);

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray);

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

canny = cv.Canny(blur, 125,175)
cv.imshow("Canny Edges",canny)

#try to binarize image to either 0 or 255
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')
print(img.shape)
blank = np.zeros(img.shape,dtype='uint8')

cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow("Blank",blank)

cv.waitKey(0);