import skimage
import numpy as np
import cv2 as cv

# 말(Horse) 이진 영상 불러오기
orig = skimage.data.horse()

# Boolean 영상을 0~255 범위의 uint8 영상으로 변환
# 흑백 반전
img = 255 - np.uint8(orig) * 255

# 원본 영상 출력
cv.imshow('Horse', img)

# 이진 영상에서 외곽 윤곽선 검출
contours, hierarchy = cv.findContours(
    img,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_NONE
)

# 컬러 디스플레이용 영상 생성
img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# 검출한 윤곽선을 자홍색으로 표시
cv.drawContours(img2, contours, -1, (255, 0, 255), 2)

cv.imshow('Horse with contour', img2)

# 첫 번째 윤곽선 선택
contour = contours[0]

# 윤곽선의 모멘트 계산
m = cv.moments(contour)

# 객체의 면적 계산
area = cv.contourArea(contour)

# 객체의 무게중심 계산
cx, cy = m['m10'] / m['m00'], m['m01'] / m['m00']

# 윤곽선의 둘레 계산
perimeter = cv.arcLength(contour, True)

# 둥근 정도 계산
roundness = (4.0 * np.pi * area) / (perimeter * perimeter)

# 특징 출력
print(
    '면적=', area,
    '\n중심=', (cx, cy),
    '\n둘레=', perimeter,
    '\n둥근 정도=', roundness
)

# 컬러 디스플레이용 영상 생성
img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# 윤곽선을 직선으로 근사
contour_approx = cv.approxPolyDP(contour, 8, True)

# 근사한 윤곽선을 초록색으로 표시
cv.drawContours(img3, [contour_approx], -1, (0, 255, 0), 2)

# 볼록 헐(Convex Hull) 계산
hull = cv.convexHull(contour)

# 볼록 헐의 배열 형태 변경
hull = hull.reshape(1, hull.shape[0], hull.shape[2])

# 볼록 헐을 빨간색으로 표시
cv.drawContours(img3, hull, -1, (0, 0, 255), 2)

# 결과 출력
cv.imshow('Horse with line segments and convex hull', img3)

cv.waitKey(0)
cv.destroyAllWindows()