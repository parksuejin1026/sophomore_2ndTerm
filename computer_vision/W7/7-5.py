import skimage
import numpy as np
import cv2 as cv
import time

# 암스테르담 이미지 불러오기
img = cv.imread('amsterdam.jpg')

# BGR 이미지를 RGB로 변환
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 실행 시간 측정 시작
start = time.time()

# SLIC 알고리즘으로 슈퍼픽셀 생성
slic = skimage.segmentation.slic(
    img,
    compactness=30,
    n_segments=600,
    start_label=1
)

# 슈퍼픽셀을 노드로 하는 영역 인접 그래프(RAG) 생성
g = skimage.graph.rag_mean_color(
    img,
    slic,
    mode='similarity'
)

# 정규화 절단 알고리즘을 이용한 영역 분할
ncut = skimage.graph.cut_normalized(slic, g)

# 이미지 크기와 실행 시간 출력
print(img.shape, '영상을 분할하는 데',
      time.time() - start, '초 소요')

# 분할된 영역의 경계선 표시
marking = skimage.segmentation.mark_boundaries(img, ncut)

# 실수형 이미지를 uint8(0~255)로 변환
ncut_img = np.uint8(marking * 255.0)

# RGB를 BGR로 변환하여 결과 출력
cv.imshow('Normalized cut',
          cv.cvtColor(ncut_img, cv.COLOR_RGB2BGR))

cv.waitKey(0)
cv.destroyAllWindows()