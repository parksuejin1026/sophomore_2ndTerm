
import cv2 as cv

# 1. 이미지 불러오기
img = cv.imread('image.jpg')

# 2. 그레이스케일 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 3. SIFT 객체 생성
sift = cv.SIFT_create()

# 4. 특징점과 기술자 추출
kp, des = sift.detectAndCompute(gray, None)

# 5. 특징점 시각화
gray = cv.drawKeypoints(
    gray,
    kp,
    None,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# 6. 결과 출력
cv.imshow('sift', gray)

cv.waitKey(0)
cv.destroyAllWindows()
