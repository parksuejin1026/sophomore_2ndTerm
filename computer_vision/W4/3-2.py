import cv2 as cv
import sys

img = cv.imread('peyz.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('original_RGB', img)
cv.imshow('Upper left half', img[0 : img.shape[0] // 2, 0:img.shape[1] // 2, :])
cv.imshow('Center half', img[img.shape[0] // 4 : 3 * img.shape[0] // 4, img.shape[1] // 4 : 3 * img.shape[ 1]// 4, :])
# 이미지의 우측 하단이면서 R 채널 부분만 남기고 창에 띄우기
cv.imshow('Right, R channel', img[img.shape[0] // 2 : , img.shape[1] // 2:, 2])
cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()
