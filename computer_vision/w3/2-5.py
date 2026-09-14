import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_MSMF) # 실습실 웹캠은 이 코드로 해야됨

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

frames = [] # 사진을 저장할 곳

while True:
    ret, frame = cap.read() 
    
    if not ret: # 프레임 가져온 것의 성공 여부 T / F
        print("프레임 획득에 실패하여 루프를 나갑니다.")
        break
    
    # 좌우 반전
    frame = cv.flip(frame, 1)
    
    cv.imshow('Video display', frame) # 영상 보여주기
    
    key = cv.waitKey(1)
    if key == ord('c'):
        frames.append(frame)
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))): # 1~3 4개 이상이 되면 3개로 고정
        imgs = np.hstack((imgs, frames[i]))
        
    cv.imshow('20251285 PSJ', imgs)
    cv.waitKey()
    cv.destroyAllWindows()
    
# 과제 창 이름을 자신의 학번 이름으로 지정
