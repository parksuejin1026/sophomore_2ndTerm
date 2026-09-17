from ArrayStack import ArrayStack   # ArrayStack.py에서 ArrayStack 클래스 불러오기


def checkBrackets(statement):       # 문자열의 괄호가 올바른지 검사하는 함수

    stack = ArrayStack(100)         # 최대 100개의 괄호를 저장할 스택 생성

    for ch in statement:            # 문자열의 문자를 하나씩 확인

        # 왼쪽 괄호를 만나면 스택에 저장 
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch)

        # 오른쪽 괄호를 만나면 괄호의 짝 검사
        elif ch == '}' or ch == ']' or ch == ')':

            # 오른쪽 괄호가 나왔는데 스택이 비어 있으면
            # 짝이 되는 왼쪽 괄호가 없으므로 False
            if stack.isEmpty():
                return False

            else:
                # 가장 최근에 저장된 왼쪽 괄호를 꺼냄 
                left = stack.pop()

                # 현재 오른쪽 괄호와
                # 스택에서 꺼낸 왼쪽 괄호의 종류가 맞지 않으면 False
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "("):
                    return False

    # 모든 문자를 검사한 후
    # 스택이 비어 있으면 모든 괄호의 짝이 맞으므로 True
    # 괄호가 남아 있으면 짝이 맞지 않으므로 False
    return stack.isEmpty()