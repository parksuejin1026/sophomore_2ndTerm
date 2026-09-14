import cv2 as cv
import sys

img = cv.imread('peyz.jpg')

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize = (0, 0), fx = 0.5, fy = 0.5)
# 추가 과제 : 컬러 이미지를 세로 3배 가로 0.5배 그림 출력
color3 = cv.resize(img, dsize = (0,0), fx = 0.5, fy = 3)

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)
# 추가 과제 : 컬러 이미지를 세로 3배 가로 0.5배 그림 출력
cv.imwrite('Color3.jpg', color3)
cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)
# 추가 과제 : 컬러 이미지를 세로 3배 가로 0.5배 그림 출력
cv.imshow('Color3', color3)

cv.waitKey()
cv.destroyAllWindows()
