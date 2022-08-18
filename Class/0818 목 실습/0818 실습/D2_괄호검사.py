import sys
sys.stdin = open("괄호_input.txt", "r")

def check(data):
    stack = []
    for i in range(len(data)):
        # 왼쪽괄호 일때 : push

        if data[i] == '(' or data[i] == '{':
            stack.append(data[i])

        # 오른쪽괄호 일때 : pop
        elif data[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif data[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    # stack에 남아 있으면 0
    if stack:
        return 0
    else:
        return 1

t = int(input())
for tc in range(t):
    string = input()
    print(f'#{tc+1} {check(string)}')
