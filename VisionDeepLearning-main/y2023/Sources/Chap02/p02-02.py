# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

read and display images

"""
import cv2 as cv
import sys

file_name = 'D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\soccer.jpg'
file_name2 = 'D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\smile_girl.jpg'
img = cv.imread(file_name)
img2 = cv.imread(file_name2)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))
if img is None:
    sys.exit('파일({0})를 찾을 수 없습니다.'.format(file_name2))

    
cv.imshow('Image Disply', img)
cv.imshow('Image Display2', img2)
    
cv.waitKey()
cv.destroyAllWindows()    
