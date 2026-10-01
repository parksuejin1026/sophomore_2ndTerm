# MazeBFS.py

from CircularQueue import *


# 이동할 수 있는 위치인지 검사
def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True

    return False


# 너비 우선 탐색
def BFS():
    que = CircularQueue()

    # 시작 위치
    que.enqueue((0, 1))

    print('BFS:')

    while not que.isEmpty():

        # 큐에서 가장 먼저 들어온 위치 꺼냄
        here = que.dequeue()

        print(here, end=' -> ')

        x, y = here

        # 출구 발견
        if map[y][x] == 'x':
            return True

        else:
            # 방문 표시
            map[y][x] = '.'

            # 상
            if isValidPos(x, y - 1):
                que.enqueue((x, y - 1))

            # 하
            if isValidPos(x, y + 1):
                que.enqueue((x, y + 1))

            # 좌
            if isValidPos(x - 1, y):
                que.enqueue((x - 1, y))

            # 우
            if isValidPos(x + 1, y):
                que.enqueue((x + 1, y))

        print('현재 큐:', que)

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


result = BFS()

if result:
    print('\n--> 미로탐색 성공')
else:
    print('\n--> 미로탐색 실패')