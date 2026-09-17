from ArrayStack import ArrayStack   # ArrayStack 클래스 불러오기


# 미로 생성
# 1 : 벽
# 0 : 이동할 수 있는 길
# e : 시작점
# x : 출구
map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

MAZE_SIZE = 6

# 이동할 수 있는 위치인지 검사
def isValidPos(x, y):

    # 미로 범위를 벗어나면 이동 불가능
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False

    # 0(길) 또는 x(출구)이면 이동 가능
    else:
        return map[y][x] == '0' or map[y][x] == 'x'
    
def DFS():

    print('DFS: ')

    stack = ArrayStack(100)   # 탐색할 위치를 저장할 스택 생성

    stack.push((0, 1))        # 시작 위치 (0, 1)을 스택에 저장

    while not stack.isEmpty():

        here = stack.pop()    # 가장 최근에 저장한 위치를 꺼냄

        print(here, end='->')

        (x, y) = here         # 현재 위치의 x, y 좌표 저장

        # 현재 위치가 출구라면 탐색 성공
        if map[y][x] == 'x':
            return True

        else:
            # 현재 위치를 방문했다는 의미로 '.' 표시
            map[y][x] = '.'

            # 위쪽으로 이동 가능한지 검사
            if isValidPos(x, y - 1):
                stack.push((x, y - 1))

            # 아래쪽으로 이동 가능한지 검사
            if isValidPos(x, y + 1):
                stack.push((x, y + 1))

            # 왼쪽으로 이동 가능한지 검사
            if isValidPos(x - 1, y):
                stack.push((x - 1, y))

            # 오른쪽으로 이동 가능한지 검사
            if isValidPos(x + 1, y):
                stack.push((x + 1, y))

            print('현재 스택:', stack)

    # 스택이 비었는데 출구를 못 찾았다면 실패
    return False

result = DFS()

if result:
    print(' --> 미로탐색 성공')

else:
    print(' --> 미로탐색 실패')