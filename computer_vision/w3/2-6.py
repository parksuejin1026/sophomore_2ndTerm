import cv2 as cv
import sys

# 이미지 파일 불러오기
img = cv.imread('peyz.jpg')

# 이미지를 정상적으로 불러오지 못한 경우 프로그램 종료
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# 이미지 위에 사각형 그리기
# 시작 좌표: (200, 30)
# 끝 좌표: (500, 400)
# 색상: (0, 0, 255) → 빨간색(BGR)
# 두께: 2
cv.rectangle(img, (200, 30), (500, 400), (0, 0, 255), -1)

# 이미지 위에 문자열 작성
# 문자열: 'peyz'
# 시작 위치: (200, 24)
# 폰트: FONT_HERSHEY_SIMPLEX
# 글자 크기: 1
# 색상: (255, 0, 0) → 파란색(BGR)
# 두께: 2
cv.putText(
    img,
    'peyz',
    (200, 24),
    cv.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 0, 0),
    2
)

# 결과 이미지 화면에 출력
cv.imshow('Draw', img)

# 키 입력이 있을 때까지 대기
cv.waitKey()

# 생성된 모든 OpenCV 창 닫기
cv.destroyAllWindows()