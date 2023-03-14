import cv2 as cv
import sys

file_name = './soccer.jpg'
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

small1 = cv.resize(dsize=(0,0), fx=0.1, fy=0.1)
small2 = cv.resize(dsize=(0,0), fx=0.2, fy=0.2)
small3 = cv.resize(dsize=(0,0), fx=0.3, fy=0.3)
small4 = cv.resize(dsize=(0,0), fx=0.4, fy=0.4)
small5 = cv.resize(dsize=(0,0), fx=0.5, fy=0.5)
small6 = cv.resize(dsize=(0,0), fx=0.6, fy=0.6)
small7 = cv.resize(dsize=(0,0), fx=0.7, fy=0.7)
small8 = cv.resize(dsize=(0,0), fx=0.8, fy=0.8)
small9 = cv.resize(dsize=(0,0), fx=0.9, fy=0.9)

    
cv.imshow('Color Image', img)
cv.imshow('Image Small', small1)
cv.imshow('Image Small', small2)
cv.imshow('Image Small', small3)
cv.imshow('Image Small', small4)
cv.imshow('Image Small', small5)
cv.imshow('Image Small', small6)
cv.imshow('Image Small', small7)
cv.imshow('Image Small', small8)
cv.imshow('Image Small', small9)  
  
cv.waitKey()
cv.destroyAllWindows()    
