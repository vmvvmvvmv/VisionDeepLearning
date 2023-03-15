# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

GUI

"""
import cv2 as cv
import sys

#file_name = './Chap02/smile_girl.jpg' # for VSCODE working directory is Chap02
file_name = 'D:\VisionDeepLearning-main\y2023\Sources\Chap02\picture\smile_girl.jpg' # for jupyter or ipython(spyder)
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

cv.rectangle(img, (580,100), (880,530), (0,0,255), 2)
cv.putText(img, 'laugh', (580,60), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
cv.arrowedLine(img,(600,65),(600,95),(0,0,255),3)

cv.imshow('Draw', img)
cv.waitKey()
cv.destroyAllWindows()    
