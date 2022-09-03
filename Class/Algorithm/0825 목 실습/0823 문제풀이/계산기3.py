import sys; sys.stdin = open('계산기3_input.txt')

icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

def infix_to_postfix(exp):
    stack = []
    result = []
    for token in exp:
        # 피연산자
        if '0' <= token <= '9':
            result.append(token)
        # 오른쪽 괄호
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        # 왼쪽괄호, 사칙연산자
        else:
            if stack:
                while icp[token] <= isp[stack[-1]]:
                    result.append(stack.pop())
                    if not stack: break
            stack.append(token)
    # 스택에 남아있으면
    while stack:
        result.append(stack.pop())
    return ''.join(result)

def calc(exp):
    stack = []
    for token in exp:
        # 피연산자 : push
        if '0' <= token <= '9':
            stack.append(int(token))
        # 연산자: 2개 pop -> 계산 -> push
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(op1 / op2)
    return stack.pop()

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()  # 중위표기식
    postfix = infix_to_postfix(infix) # 후위표기식
    print(f'#{tc} {calc(postfix)}')
