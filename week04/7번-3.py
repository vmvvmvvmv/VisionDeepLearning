import cv2 as cv

img = cv.imread('soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x = cv.Scharr(gray, cv.CV_32F, 1, 0)  # Scharr 연산자 적용
grad_y = cv.Scharr(gray, cv.CV_32F, 0, 1)
grad_x1 = cv.Sobel(gray,cv.CV_32F,1,0,ksize=3) # Sobel 연산자 적용
grad_y1 = cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

scharr_x = cv.convertScaleAbs(grad_x)  # 절대값을 취해 양수 영상으로 변환
scharr_y = cv.convertScaleAbs(grad_y)
sobel_x = cv.convertScaleAbs(grad_x1)	
sobel_y = cv.convertScaleAbs(grad_y1)

edge_strength = cv.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)  # 에지 강도 계산
edge_strength2 = cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)

cv.imshow('Original', gray)
cv.imshow('Scharr_x', scharr_x)
cv.imshow('Scharr_y', scharr_y)
cv.imshow('Sobel_x', sobel_x)
cv.imshow('Sobel_y', sobel_y)
cv.imshow('Edge strength', edge_strength)
cv.imshow('Edge strength2', edge_strength2)

cv.waitKey()
cv.destroyAllWindows()