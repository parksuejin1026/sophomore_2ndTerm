import cv2 as cv
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv.imread('peyz.jpg')


# BGR 컬러 영상을 명암(Grayscale) 영상으로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 흑백 영상 출력
plt.imshow(gray, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()


# 원본 흑백 영상의 히스토그램 계산
h = cv.calcHist(
    [gray],     # 입력 영상
    [0],        # 사용할 채널
    None,       # 마스크 없음
    [256],      # 히스토그램 구간 수
    [0, 256]    # 픽셀 값 범위
)

# 원본 영상의 히스토그램 출력
plt.plot(h, color='r', linewidth=1)
plt.show()


# 히스토그램 평활화 수행
equal = cv.equalizeHist(gray)

# 평활화된 영상 출력
plt.imshow(equal, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()


# 평활화된 영상의 히스토그램 계산
h = cv.calcHist(
    [equal],
    [0],
    None,
    [256],
    [0, 256]
)

# 평활화 후 히스토그램 출력
plt.plot(h, color='r', linewidth=1)
plt.show()