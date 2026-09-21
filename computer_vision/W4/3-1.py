import cv2 as cv
import numpy as np

img = cv.imread('peyz.jpg')

print("shape : ", img.shape) # (세로, 가로, 색 채널)로 출력
print("최솟값 : ", img.min())
print("최댓값 : ", img.max())
print("평균 : ", img.mean())

print("최댓값 위치 : ", np.argmax(img))

print("정렬 후 앞 부분 : ", np.sort(img, axis = None)[:10])

transposed = np.transpose(img, (1, 0, 2)) # 가로 세로 변환

print("가로 세로 변환 후 모양 : ", transposed.shape)

cv.imshow("Original", img)
cv.imshow("Transposed", transposed)

cv.waitKey()
cv.destroyAllWindows()