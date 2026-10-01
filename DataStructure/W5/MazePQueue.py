# MazePQueue.py

from PriorityQueue import PriorityQueue
import math


# 출구 위치
ox, oy = 5, 4


# 현재 위치와 출구 사이 거리
def dist(x, y):

    dx = ox - x
    dy = oy - y

    # 거리가 가까울수록 큰 값이 되도록 음수 사용
    return -math.sqrt(dx * dx + dy * dy)


# 이동 가능한 위치인지 검사
def isValidPos(x, y):

    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:

        if map[y][x] == '0' or map[y][x] == 'x':
            return True

    return False


# 전략적 미로 탐색
def MySmartSearch():

    q = PriorityQueue()

    # 시작 위치
    q.enqueue((0, 1, dist(0, 1)))

    print('PQueue:')

    while not q.isEmpty():

        here = q.dequeue()

        # 좌표만 출력
        print(here[0:2], end=' -> ')

        x, y, _ = here

        # 출구 도착
        if map[y][x] == 'x':
            return True

        else:

            # 방문한 위치 표시
            map[y][x] = '.'

            # 위
            if isValidPos(x, y - 1):
                q.enqueue(
                    (x, y - 1, dist(x, y - 1))
                )

            # 아래
            if isValidPos(x, y + 1):
                q.enqueue(
                    (x, y + 1, dist(x, y + 1))
                )

            # 왼쪽
            if isValidPos(x - 1, y):
                q.enqueue(
                    (x - 1, y, dist(x - 1, y))
                )

            # 오른쪽
            if isValidPos(x + 1, y):
                q.enqueue(
                    (x + 1, y, dist(x + 1, y))
                )

        print('우선순위큐:', q)

    return False


# 미로
map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]

MAZE_SIZE = 6


result = MySmartSearch()

if result:
    print('\n--> 미로탐색 성공')
else:
    print('\n--> 미로탐색 실패')