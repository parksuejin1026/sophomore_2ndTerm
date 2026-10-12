import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('amsterdam.jpg')
img_show = np.copy(img)  # 붓칠을 표시할 이미지 복사

# 이미지 크기에 맞는 마스크 생성
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

# 모든 화소를 '아마도 배경'으로 초기화
mask[:, :] = cv.GC_PR_BGD

# 붓 크기 설정
BrushSiz = 9

# 물체(파란색), 배경(빨간색) 표시 색상
LColor, RColor = (255, 0, 0), (0, 0, 255)


# 마우스로 물체와 배경을 지정하는 함수
def painting(event, x, y, flags, param):

    # 왼쪽 마우스 클릭: 물체 표시
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)

    # 오른쪽 마우스 클릭: 배경 표시
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)

    # 왼쪽 버튼을 누른 채 이동: 물체 영역 칠하기
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)

    # 오른쪽 버튼을 누른 채 이동: 배경 영역 칠하기
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)

    # 붓칠한 이미지 출력
    cv.imshow('Painting', img_show)


# 마우스 이벤트 등록
cv.namedWindow('Painting')
cv.setMouseCallback('Painting', painting)
cv.imshow('Painting', img_show)

# q 키를 누를 때까지 붓칠 진행
while True:
    if cv.waitKey(1) == ord('q'):
        break


# GrabCut 알고리즘 적용

# 배경과 물체의 모델을 저장할 배열 초기화
background = np.zeros((1, 65), np.float64)
foreground = np.zeros((1, 65), np.float64)

# GrabCut 수행 (5회 반복)
cv.grabCut(
    img,
    mask,
    None,
    background,
    foreground,
    5,
    cv.GC_INIT_WITH_MASK
)

# 배경은 0, 물체는 1로 변환
mask2 = np.where(
    (mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD),
    0,
    1
).astype('uint8')

# 원본 이미지에서 물체 영역만 남기기
grab = img * mask2[:, :, np.newaxis]

# 최종 결과 출력
cv.imshow('Grab cut image', grab)

cv.waitKey(0)
cv.destroyAllWindows()