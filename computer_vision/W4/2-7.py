import cv2 as cv
import sys

img = cv.imread('peyz.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
def draw(event, x, y, flags, param): # 콜백 함수
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x + 50), (y + 50), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.retangle(img, (x, y), (x + 50, y + 50), (255, 0, 0), 2) # -1 로 지정한다면 내부에 색을 채운 사각형
        
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if  cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break