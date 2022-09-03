def forth(code):
    stack = []
    for token in code:
        # 정수
        if token.isdigit():
            stack.append(token)
        # 사칙연산자
        elif token == '+' or token == '-' or token == '*' or token == '/':
            if len(stack) >= 2:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    stack.append(op1 // op2)    # / 와 // 구분! 조심하기!
            else:
                return 'error'
        # 점(.)
        elif token == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'


T = int(input())
for tc in range(1, T + 1):
    code = list(input().split())
    # print(code)
    print(f'#{tc} {forth(code)}')