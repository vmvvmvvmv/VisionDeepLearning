import cv2 as cv 
import numpy as np

img = cv.imread('soccer.jpg')  # 영상 읽기
img_show = np.copy(img)  # 붓 칠을 디스플레이할 목적의 영상
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8) 
mask[:, :] = cv.GC_PR_BGD  # 모든 화소를 배경일 것 같음으로 초기화
BrushSiz = 9  # 붓의 크기
LColor, RColor = (255, 0, 0), (0, 0, 255)  # 파란색(물체)과 빨간색(배경)

def update_mask(event, x, y, flags, param):
    global img_show, mask
    
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img_show, (x,y), BrushSiz, LColor, -1)
        cv.circle(mask, (x,y), BrushSiz, cv.GC_FGD, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show, (x,y), BrushSiz, RColor, -1)
        cv.circle(mask, (x,y), BrushSiz, cv.GC_BGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show, (x,y), BrushSiz, LColor, -1)
        cv.circle(mask, (x,y), BrushSiz, cv.GC_FGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show, (x,y), BrushSiz, RColor, -1)
        cv.circle(mask, (x,y), BrushSiz, cv.GC_BGD, -1)

    cv.imshow('Painting', img_show)

def grabcut_iteration(img, mask):
    global BrushSiz, LColor, RColor
    
    while True:
        cv.imshow('Painting', img_show)
        key = cv.waitKey(1)

        if key == ord('q'):
            cv.destroyAllWindows()
            break
        elif key == ord('r'):
            mask[:] = cv.GC_PR_BGD  # 모든 화소를 배경일 것 같음으로 초기화
            img_show[:] = img  # 붓 칠을 디스플레이할 목적의 영상 초기화
            
        elif key == ord('w'):
            background = np.zeros((1, 65), np.float64)  # 배경 히스토그램 0으로 초기화
            foreground = np.zeros((1, 65), np.float64)  # 물체 히스토그램 0으로 초기화
            cv.grabCut(img, mask, None, background, foreground, 1, cv.GC_INIT_WITH_MASK)
            mask2 = np.where((mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD), 0, 1).astype('uint8')
            grab = img * mask2[:,:,np.newaxis]
            cv.imshow('Grab cut image', grab)
            

        cv.setMouseCallback('Painting', update_mask)
cv.namedWindow('Painting')
cv.setMouseCallback('Painting', update_mask)

while True:
    grabcut_iteration(img, mask)
    break