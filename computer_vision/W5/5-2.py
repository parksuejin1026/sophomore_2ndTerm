import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('peyz.jpg')

# 이미지 크기를 25%로 축소
img = cv.resize(img, dsize=(0, 0), fx=0.25, fy=0.25)


# 감마 보정 함수
def gamma(f, gamma=1.0):
    # 픽셀 값을 0~1 범위로 정규화
    f1 = f / 255.0

    # 감마 보정 후 다시 0~255 범위로 변환
    return np.uint8(255 * (f1 ** gamma))


# 서로 다른 감마 값을 적용한 영상들을 가로로 연결
gc = np.hstack((
    gamma(img, 0.5),
    gamma(img, 0.75),
    gamma(img, 1.0),
    gamma(img, 2.0),
    gamma(img, 3.0)
))

# 결과 영상 출력
cv.imshow('gamma', gc)

# 키 입력 대기
cv.waitKey()

# 모든 OpenCV 창 닫기
cv.destroyAllWindows()