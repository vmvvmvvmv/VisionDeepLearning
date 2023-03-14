# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

GUI

"""
import cv2 as cv
import sys

#file_name = './Chap02/smile_girl.jpg' # for VSCODE working directory is Chap02
file_name = './soccer.jpg' # for jupyter or ipython(spyder)
img = cv.imread(file_name)
if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

BrushSize = 5
LColor, RColor = (255,0,0), (0,0,255)
def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, RColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSize, RColor, -1)
    cv.imshow('Painting', img)

cv.namedWindow('Painting')
cv.imshow('Painting', img)

cv.setMouseCallback('Painting', painting)

while(True):
    if cv.waitKey(1) == ord('q'):        
        cv.destroyAllWindows()
        break
