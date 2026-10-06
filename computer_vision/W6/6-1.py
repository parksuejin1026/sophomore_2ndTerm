import cv2 as cv

# 이미지 불러오기
img = cv.imread('oner.png')

# 이미지에서 특정 영역 잘라내기
# 행(y): 250~349, 열(x): 170~269 영역 추출
# ':'는 B, G, R의 모든 색상 채널을 사용한다는 의미
patch = img[250:350, 170:270, :]


# 원본 이미지에서 잘라낸 영역을 파란색 사각형으로 표시
# 시작점 (170, 250), 끝점 (270, 350)
# 색상 (255, 0, 0) = BGR 기준 파란색
# 선 두께 = 3
img = cv.rectangle(img, (170, 250), (270, 350), (255, 0, 0), 3)


# -------------------------------------------------
# 잘라낸 영역(patch)을 가로·세로 각각 5배 확대
# -------------------------------------------------

# 최근접 이웃 보간법(Nearest Neighbor)
# 가장 가까운 픽셀 값을 그대로 사용하여 확대
# 계산은 빠르지만 확대하면 픽셀이 계단처럼 보일 수 있음
patch1 = cv.resize(
    patch,
    dsize=(0, 0),
    fx=5,
    fy=5,
    interpolation=cv.INTER_NEAREST
)

# 양선형 보간법(Bilinear Interpolation)
# 주변 픽셀 값을 이용하여 새로운 픽셀 값을 계산
# 최근접 이웃보다 부드러운 결과를 얻을 수 있음
patch2 = cv.resize(
    patch,
    dsize=(0, 0),
    fx=5,
    fy=5,
    interpolation=cv.INTER_LINEAR
)

# 바이큐빅 보간법(Bicubic Interpolation)
# 주변의 더 많은 픽셀을 이용하여 새로운 픽셀 값을 계산
# 계산량은 많지만 확대할 때 비교적 부드럽고 선명함
patch3 = cv.resize(
    patch,
    dsize=(0, 0),
    fx=5,
    fy=5,
    interpolation=cv.INTER_CUBIC
)


# 원본 이미지 출력
cv.imshow('Original', img)

# 최근접 이웃 보간법으로 확대된 이미지 출력
cv.imshow('Resize nearest', patch1)

# 양선형 보간법으로 확대된 이미지 출력
cv.imshow('Resize bilinear', patch2)

# 바이큐빅 보간법으로 확대된 이미지 출력
cv.imshow('Resize bicubic', patch3)


# 키보드 입력이 있을 때까지 결과 창 유지
cv.waitKey()

# 모든 OpenCV 창 닫기
cv.destroyAllWindows()import cv2 as cv

# 이미지 불러오기
img = cv.imread('oner.png')

# 이미지에서 특정 영역 잘라내기
# 행(y): 250~349, 열(x): 170~269 영역 추출
# ':'는 B, G, R의 모든 색상 채널을 사용한다는 의미
patch = img[250:350, 170:270, :]


# 원본 이미지에서 잘라낸 영역을 파란색 사각형으로 표시
# 시작점 (170, 250), 끝점 (270, 350)
# 색상 (255, 0, 0) = BGR 기준 파란색
# 선 두께 = 3
img = cv.rectangle(img, (170, 250), (270, 350), (255, 0, 0), 3)


# -------------------------------------------------
# 잘라낸 영역(patch)을 가로·세로 각각 5배 확대
# -------------------------------------------------

# 최근접 이웃 보간법(Nearest Neighbor)
# 가장 가까운 픽셀 값을 그대로 사용하여 확대
# 계산은 빠르지만 확대하면 픽셀이 계단처럼 보일 수 있음
patch1 = cv.resize(
    patch,
    dsize=(0, 0),
    fx=5,
    fy=5,
    interpolation=cv.INTER_NEAREST
)

# 양선형 보간법(Bilinear Interpolation)
# 주변 픽셀 값을 이용하여 새로운 픽셀 값을 계산
# 최근접 이웃보다 부드러운 결과를 얻을 수 있음
patch2 = cv.resize(
    patch,
    dsize=(0, 0),
    fx=5,
    fy=5,
    interpolation=cv.INTER_LINEAR
)

# 바이큐빅 보간법(Bicubic Interpolation)
# 주변의 더 많은 픽셀을 이용하여 새로운 픽셀 값을 계산
# 계산량은 많지만 확대할 때 비교적 부드럽고 선명함
patch3 = cv.resize(
    patch,
    dsize=(0, 0),
    fx=5,
    fy=5,
    interpolation=cv.INTER_CUBIC
)


# 원본 이미지 출력
cv.imshow('Original', img)

# 최근접 이웃 보간법으로 확대된 이미지 출력
cv.imshow('Resize nearest', patch1)

# 양선형 보간법으로 확대된 이미지 출력
cv.imshow('Resize bilinear', patch2)

# 바이큐빅 보간법으로 확대된 이미지 출력
cv.imshow('Resize bicubic', patch3)


# 키보드 입력이 있을 때까지 결과 창 유지
cv.waitKey()

# 모든 OpenCV 창 닫기
cv.destroyAllWindows()