import sys; sys.stdin = open('쇠막대기_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    cnt = 0
    stack = []
    for i in range(len(arr)):
        if arr[i] == '(':   # 왼쪽괄호
            stack.append(arr[i])
        else:               # 오른쪽 괄호
            stack.pop()
            if arr[i-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
    print(f'#{tc} {cnt}')

