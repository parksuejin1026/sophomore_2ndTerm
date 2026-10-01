# CircularDeque.py

from CircularQueue import *


class CircularDeque(CircularQueue):

    def __init__(self, capacity=10):
        super().__init__(capacity)

    # =========================
    # 기존 Queue 기능 재사용
    # =========================

    # 후단 삽입
    def addRear(self, item):
        self.enqueue(item)

    # 전단 삭제
    def deleteFront(self):
        return self.dequeue()

    # 전단 확인
    def getFront(self):
        return self.peek()

    # =========================
    # Deque에서 추가되는 기능
    # =========================

    # 전단 삽입
    def addFront(self, item):

        if not self.isFull():

            # 현재 front 위치에 데이터 저장
            self.array[self.front] = item

            # front를 반시계 방향으로 이동
            self.front = (
                self.front - 1 + self.capacity
            ) % self.capacity

        else:
            print("Deque is Full")

    # 후단 삭제
    def deleteRear(self):

        if not self.isEmpty():

            # rear 위치의 데이터 저장
            item = self.array[self.rear]

            # rear를 반시계 방향으로 이동
            self.rear = (
                self.rear - 1 + self.capacity
            ) % self.capacity

            return item

        else:
            print("Deque is Empty")

    # 후단 데이터 확인
    def getRear(self):

        if not self.isEmpty():
            return self.array[self.rear]


# 테스트
if __name__ == "__main__":

    dq = CircularDeque()

    # 0 ~ 8
    for i in range(9):

        # 짝수 → 후단
        if i % 2 == 0:
            dq.addRear(i)

        # 홀수 → 전단
        else:
            dq.addFront(i)

    print("홀수->전단, 짝수->후단:", dq)

    # 전단 두 번 삭제
    for i in range(2):
        dq.deleteFront()

    # 후단 세 번 삭제
    for i in range(3):
        dq.deleteRear()

    print("전단삭제x2 후단삭제x3:", dq)

    # 9 ~ 13 전단 삽입
    for i in range(9, 14):
        dq.addFront(i)

    print("전단삽입 9,10,...13:", dq)