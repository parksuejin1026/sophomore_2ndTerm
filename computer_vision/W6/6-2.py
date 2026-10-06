import cv2 as cv

# 이미지 파일 불러오기
img = cv.imread('oner.png')

# 컬러 이미지를 흑백(Gray Scale) 이미지로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# -----------------------------
# Sobel 연산자를 이용한 에지 검출
# -----------------------------

# x축 방향으로 밝기 변화량 계산
# dx=1, dy=0 → x방향 미분
# 주로 세로 방향의 경계(에지)를 검출
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)

# y축 방향으로 밝기 변화량 계산
# dx=0, dy=1 → y방향 미분
# 주로 가로 방향의 경계(에지)를 검출
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)


# -----------------------------
# 음수 값을 양수로 변환
# -----------------------------

# x방향 미분 결과의 절댓값을 구하고
# 화면에 출력할 수 있는 8비트 영상으로 변환
sobel_x = cv.convertScaleAbs(grad_x)

# y방향 미분 결과의 절댓값을 구하고
# 화면에 출력할 수 있는 8비트 영상으로 변환
sobel_y = cv.convertScaleAbs(grad_y)


# -----------------------------
# x, y 방향 에지 결합
# -----------------------------

# x방향 에지와 y방향 에지를 각각 0.5 비율로 합침
# 전체적인 영상의 에지 강도를 생성
edge_strength = cv.addWeighted(
    sobel_x, 0.5,
    sobel_y, 0.5,
    0
)


# -----------------------------
# 결과 영상 출력
# -----------------------------

# 원본 이미지를 흑백으로 출력
cv.imshow('Original', gray)

# x방향 Sobel 결과 출력
cv.imshow('sobel x', sobel_x)

# y방향 Sobel 결과 출력
cv.imshow('sobel y', sobel_y)

# x, y 방향 에지를 합친 결과 출력
cv.imshow('edge strength', edge_strength)


# 키보드 입력이 들어올 때까지 창 유지
cv.waitKey()

# 생성된 모든 OpenCV 창 닫기
cv.destroyAllWindows()