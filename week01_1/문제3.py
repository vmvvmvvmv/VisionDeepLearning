import cv2 as cv
import sys

file_name = './soccer.jpg'
file_name2 = './smile_girl.jpg'
img = cv.imread(file_name)
img2 =cv.imread(file_name2)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))
if img2 is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name2))  

cv.imshow('Image Disply', img)
cv.imshow('Image Disply', img2) 

cv.waitKey()
cv.destroyAllWindows()    
s