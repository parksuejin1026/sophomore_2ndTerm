
# 코드 8.1: 이진트리를 위한 노드 클래스
class TNode:        # 이진 트리를 위한 노드 클래스
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

    def isLeaf(self):   # 왼쪽/오른쪽 없으면 리프 노드
        return self.left is None and self.right is None

# 코드 8.2: 이진트리의 전위순회
def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

# 코드 8.3: 이진트리의 중위순회
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 코드 8.4: 이진트리의 후위순회
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 코드 8.5: 이진트리의 레벨순회
from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 코드 8.6: 이진트리의 노드 수 계산
def count_node(n) :     # 순환을 통해 트리의 노드 수 구하는 함수
    if n is None :      # n이 None 이면 공백 트리 -> 0 반환
        return 0
    else :              # 좌우 서브 트리 노드 수의 합 +1(루트) 반환
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 8.7: 이진트리의 단말노드 수 계산      
def count_leaf(n) :
    if n is None : return 0         # 공백트리 : 0 반환
    elif n.isLeaf() : return 1      # 단말노드 : 1 반환
    else : return count_leaf(n.left) + count_leaf(n.right)
                    # 비 단말노드 : 좌우 서브트리 결과의 합 반환

# 코드 8.8: 이진트리의 트리의 높이 계산
def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)     # 왼쪽 트리 높이
    hRight = calc_height(n.right)   # 오른쪽 트리 높이
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1         # 둘 중 큰거 +1(루트)


# 코드 8.9: 이진 트리 연산 테스트 프로그램
if __name__ == "__main__":

    print("\n======= 이진트리 테스트 ===================================") 
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    print('\n   In-Order : ', end='')
    inorder(root)
    print('\n  Pre-Order : ', end='')
    preorder(root)
    print('\n Post-Order : ', end='')
    postorder(root)
    print('\nLevel-Order : ', end='')
    levelorder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))

