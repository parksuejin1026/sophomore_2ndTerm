import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_MSMF) # 실습실 웹캠은 이 코드로 해야됨

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
while True:
    ret, frame = cap.read() 
    
    if not ret: # 프레임 가져온 것의 성공 여부 T / F
        print("프레임 획득에 실패하여 루프를 나갑니다.")
        break
    
    # 좌우 반전
    frame = cv.flip(frame, 1)
    
    cv.imshow('Video display', frame) # 영상 보여주기
    
    key = cv.waitKey(10)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()