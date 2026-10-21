
# 코드 7.11: 해시 테이블 및 해시 함수 준비

M = 13                      # 해시 테이블의 크기
table = [None] * M          # 크기가 13인 해시 테이블 생성

def hashFn(key):
    return key % M          # 키를 13으로 나눈 나머지를 인덱스로 사용


# 코드 7.12: 선형 조사법의 삽입 연산

def insert(key):
    i = hashFn(key)         # 해시 함수를 이용해 초기 위치 계산
    count = M               # 최대 조사 횟수

    while count > 0:
        if table[i] == None or table[i] == -1:
            break           # 빈 공간이나 삭제된 공간 발견

        i = (i + 1) % M      # 충돌 발생 시 다음 인덱스로 이동
        count -= 1          # 남은 조사 횟수 감소

    if count > 0:
        table[i] = key      # 발견한 위치에 데이터 삽입


# 코드 7.13: 선형 조사법의 탐색 연산

def search(key):
    i = hashFn(key)         # 탐색 시작 위치 계산
    count = M

    while count > 0:
        if table[i] == None:
            return None     # 빈 공간을 만나면 탐색 실패

        if table[i] == key:
            return table[i] # 데이터를 찾으면 해당 값 반환

        i = (i + 1) % M      # 다음 위치 조사
        count -= 1

    return None             # 끝까지 찾지 못하면 탐색 실패


# 코드 7.14: 선형 조사법의 삭제 연산

def delete(key):
    i = hashFn(key)         # 삭제할 데이터의 초기 위치 계산
    count = M

    while count > 0:
        if table[i] == key:
            table[i] = -1   # 삭제된 위치를 -1로 표시
            return

        if table[i] == None:
            return          # 데이터가 존재하지 않음

        i = (i + 1) % M      # 다음 위치 조사
        count -= 1


# 코드 7.15: 선형 조사법의 테스트 코드

if __name__ == "__main__":
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]

    # 데이터 삽입
    for d in data:
        print("h(%2d)=%2d" % (d, hashFn(d)), end=' ')
        insert(d)
        print(table)

    # 데이터 탐색
    print("46탐색-->", search(46))
    print("39탐색-->", search(39))

    # 데이터 삭제
    print("60삭제-->", end='')
    delete(60)
    print(table)

    print("46삭제-->", end='')
    delete(46)
    print(table)
