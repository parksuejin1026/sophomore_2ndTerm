# PriorityQueue.py

class PriorityQueue:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # 비어 있는지 확인
    def isEmpty(self):
        return self.size == 0

    # 가득 찼는지 확인
    def isFull(self):
        return self.size == self.capacity

    # 데이터 삽입
    def enqueue(self, e):

        if not self.isFull():
            self.array[self.size] = e
            self.size += 1

    # 가장 우선순위가 높은 데이터의 인덱스 찾기
    def findMaxIndex(self):

        if self.isEmpty():
            return -1

        highest = 0

        for i in range(1, self.size):

            if self.array[i] > self.array[highest]:
                highest = i

        return highest

    # 가장 우선순위가 높은 데이터 삭제
    def dequeue(self):

        highest = self.findMaxIndex()

        if highest != -1:

            self.size -= 1

            # 우선순위가 가장 높은 값과
            # 배열 마지막 값을 교환
            self.array[highest], self.array[self.size] = (
                self.array[self.size],
                self.array[highest]
            )

            return self.array[self.size]

    # 가장 우선순위가 높은 값 확인
    def peek(self):

        highest = self.findMaxIndex()

        if highest != -1:
            return self.array[highest]

    # 출력
    def __str__(self):
        return str(self.array[0:self.size])


# 테스트
if __name__ == "__main__":

    q = PriorityQueue()

    q.enqueue(34)
    q.enqueue(18)
    q.enqueue(27)
    q.enqueue(45)
    q.enqueue(15)

    print("PQueue:", q)

    while not q.isEmpty():
        print("Max Priority =", q.dequeue())