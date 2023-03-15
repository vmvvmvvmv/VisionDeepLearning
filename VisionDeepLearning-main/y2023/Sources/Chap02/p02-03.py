# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

change images

"""
import cv2 as cv
import sys

file_name = 'D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg'
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

small1 = cv.resize(img, dsize=(0,0), fx=0.1, fy=0.1)
small2 = cv.resize(img, dsize=(0,0), fx=0.2, fy=0.2)
small3 = cv.resize(img, dsize=(0,0), fx=0.3, fy=0.3)
small4 = cv.resize(img, dsize=(0,0), fx=0.4, fy=0.4)
small5 = cv.resize(img, dsize=(0,0), fx=0.5, fy=0.5)
small6 = cv.resize(img, dsize=(0,0), fx=0.6, fy=0.6)
small7 = cv.resize(img, dsize=(0,0), fx=0.7, fy=0.7)
small8 = cv.resize(img, dsize=(0,0), fx=0.8, fy=0.8)
small9 = cv.resize(img, dsize=(0,0), fx=0.9, fy=0.9)

cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small1)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small2)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small3)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small4)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small5)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small6)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small7)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small8)
cv.imwrite('D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg', small9)
    
cv.imshow('Color Image', img)
cv.imshow('Color Image1', small1)
cv.imshow('Color Image2', small2)
cv.imshow('Color Image3', small3)
cv.imshow('Color Image4', small4)
cv.imshow('Color Image5', small5)
cv.imshow('Color Image6', small6)
cv.imshow('Color Image7', small7)
cv.imshow('Color Image8', small8)
cv.imshow('Color Image9', small9)
    
cv.waitKey()
cv.destroyAllWindows()
