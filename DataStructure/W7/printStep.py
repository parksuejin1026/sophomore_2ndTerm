def printStep(arr, val):
    print(" Step %2d = " % val, end = '')
    print(arr)
    
# 코드 7-1 : 선택 정렬 알고리즘
def selection_sort(A) :
    n = len(A) # n을 A의 길이로 둠
    for i in range(n - 1): # 처음부터 마지막 전 인덱스까지 돌기
         # 현재 인덱스 저장
        least = i
        # 현재 인덱스 + 1부터 마지막 인덱스까지 반복문
        # 현재 인덱스는 least로 지정했기 때문에 사용할 이유없음
        for j in range(i + 1, n): 
            if (A[j] < A[least]): # least 인덱스의 A 요소의 값보다 작다면
                least = j # least 인덱스 값 변환
        # 최종적으로 가장 작은 값과 i인 현재 인덱스의 요소 값을 바꾸면 제일 작은 값이 저장됨
        A[i], A[least] = A[least], A[i]
        printStep(A, i + 1)

# 삽입 정렬 알고리즘
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1]  = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

# 버블 정렬 알고리즘
def bubble_sort(A) :
    # n은 A 배열의 길이
    n = len(A)
    # n - 1 인덱스부터 0까지 1씩 감소
    for i in range(n - 1, 0, -1) : # n-1 부터 0까지
        # 바뀐 지 유무
        bChanged = False
        # i 값 반복문
        for j in range (i) : # 0~i까지
            # 만약 배열의 j번째 값보다 j+1 값이 크다면
            if (A[j] > A[j+1]) :
                # 둘의 위치 바꾸기 큰 값이 뒤로감
                A[j], A[j+1] = A[j+1], A[j]
                # 바꿨으니 True로 변경
                bChanged = True
        # true면 멈추기
        if not bChanged: break
        printStep(A, n - 1)

# 이진 탐색 알고리즘 중 순환 구조
def binary_search(A, key, low, high):
    if (low > high):
        return -1
    
    middle = (low + high) // 2
    
    print(A[middle], end = ' ')
    if (key == A[middle]):
        return "middle index = " + str(middle)
    elif (key < A[middle]):
        return binary_search(A, key, low, middle - 1)
    else :
        return binary_search(A, key, middle + 1, high)

# 이진 탐색 알고리즘 중 반복 구조
def binary_search_iter(A, k, l, h):
    while (l <= h):
        m = (l + h) // 2
        print(A[m], end = ' ')
        if k == A[m]:
            return "middle index = " + str(m)
        elif( k > A[m]) :
            l = m + 1
        else:
            h = m - 1
    
    return -1
    
if __name__ == "__main__":
    # 선택 정렬 알고리즘
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    data = list(org)
    print("-- 선택 정렬 알고리즘 --")
    print("Original : ", org)
    selection_sort(data)
    print("Selection : ", data)
    
    # 삽입 정렬 알고리즘
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    data = list(org)
    print("-- 삽입 정렬 알고리즘 --")
    print("Original : ", org)
    insertion_sort(data)
    print("Selection : ", data)
    
    # 버블 정렬 알고리즘
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    data = list(org)
    print("-- 버블 정렬 알고리즘 --")
    print("Original : ", org)
    bubble_sort(data)
    print("Bubble : ", data )
    
    print("이진 탐색 알고리즘")
    array = [2, 6, 11, 13, 18, 20, 22, 27, 29, 31, 35, 41, 42, 50]
    n = len(array)
    print("입력 배열 = ", array)
    key = 31
    print("이진 탐색 %d : " %key, binary_search(array, key, 0, n-1))
    print("이진 반복 %d : " %key, binary_search_iter(array, key, 0, n - 1))