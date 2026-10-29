
# 코드 8.10: 모스 코드 표와 인코딩 알고리즘
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
    ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..')
]


# 이진 트리 노드 클래스
class TNode:
    def __init__(self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right


# 코드 8.12: 모스 코드 결정 트리 만들기
def make_morse_tree():
    root = TNode(None, None, None)

    for tp in table:
        code = tp[1]
        node = root

        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TNode(None, None, None)
                node = node.left

            elif c == '-':
                if node.right is None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]

    return root


# 인코딩: 알파벳 -> 모스 코드
def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]


# 디코딩: 모스 코드 -> 알파벳
def decode(root, code):
    node = root

    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right

    return node.data


# 코드 8.13: 모스 코드 테스트 프로그램
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()

    text = input("입력 문장(대문자) : ")

    mlist = []

    for ch in text:
        code = encode(ch)
        mlist.append(code)

    print("Morse Code: ", mlist)

    print("Decoding : ", end='')

    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')

    print()
