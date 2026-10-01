# CircularQueue.py

class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity # 용량
        self.array = [None] * capacity # 배열 기본 값 8개
        self.front = 0 # 맨 앞
        self.rear = 0 # 맨 뒤

    # 큐가 비어 있는지 확인
    def isEmpty(self): 
        return self.front == self.rear # 둘의 위치가 같다면 아무 것도 없는 것

    # 큐가 가득 찼는지 확인
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity # 프론트가 맨 앞이고 rear가 맨 끝에 있을 때 나머지 연산을 한다면 프론트의 값이되기 때문에 꽉 참

    # 후단에 데이터 삽입
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("Queue is Full")

    # 전단에서 데이터 삭제
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Queue is Empty")

    # 맨 앞 데이터 확인
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    # 현재 저장된 데이터 개수
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    # 큐 내용 출력
    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])

        else:
            return str(
                self.array[self.front + 1:self.capacity]
                + self.array[0:self.rear + 1]
            )


# 테스트 코드
if __name__ == "__main__":
    q = CircularQueue(8)

    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')

    print('A B C D E F 삽입:', q)

    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())

    print('3번의 삭제:', q)

    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')

    print('G H I 삽입:', q)