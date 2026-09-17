from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix


# 연산자의 우선순위 계산 함수
def precedence(op):

    if op == '(' or op == ')':
        return 0

    elif op == '+' or op == '-':
        return 1

    elif op == '*' or op == '/':
        return 2

    else:
        return -1
    
def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:

        # '('일 때
        if term in '(':
            s.push('(')

        # ')'일 때
        elif term in ')':

            while not s.isEmpty():
                op = s.pop()

                if op == '(':
                    break

                else:
                    output.append(op)

        # 연산자일 때
        elif term in "+-*/":

            while not s.isEmpty():
                op = s.peek()

                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()

                else:
                    break

            s.push(term)

        # 피연산자일 때
        else:
            output.append(term)

    # 스택에 남아 있는 연산자 처리
    while not s.isEmpty():
        output.append(s.pop())

    return output

if __name__ == "__main__":
    print('스택의 응용3: 중위표기식 후위표기 변환\n')
    infix1 = [ '8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = [ '1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)
    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)
    print(' 중위표기: ', infix1)
    print(' 후위표기: ', postfix1)
    print(' 계산결과: ', result1, end='\n\n')
    print(' 중위표기: ', infix2)
    print(' 후위표기: ', postfix2)
    print(' 계산결과: ', result2)