import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')
img=cv.resize(img,dsize=(0,0), fx=0.4,fy=0.4)
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.putText(gray,'soccer',(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
# cv.imshow('Original',gray)

smooth=np.hstack((cv.GaussianBlur(gray,(5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0),cv.GaussianBlur(gray,(15,15),0.0)))
Md_smooth=np.hstack((cv.medianBlur(gray,5),cv.medianBlur(gray,9),cv.medianBlur(gray,15)))
cv.imshow('Smooth',smooth)
cv.imshow('median_smoth',Md_smooth)
femboss=np.array([[-1.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 1.0]])

gray16=np.int16(gray)


cv.waitKey()
cv.destroyAllWindows()