import cv2 as cv

img = cv.imread('soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x = cv.Scharr(gray, cv.CV_32F, 1, 0)  # Scharr 연산자 적용
grad_y = cv.Scharr(gray, cv.CV_32F, 0, 1)

scharr_x = cv.convertScaleAbs(grad_x)  # 절대값을 취해 양수 영상으로 변환
scharr_y = cv.convertScaleAbs(grad_y)

edge_strength = cv.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)  # 에지 강도 계산

cv.imshow('Original', gray)
cv.imshow('Scharr_x', scharr_x)
cv.imshow('Scharr_y', scharr_y)
cv.imshow('Edge strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()