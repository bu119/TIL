T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    stack = []

    for i in range(len(str1)):
        # 스택이 비어 있으면
        if len(stack) == 0:
            stack.append(str1[i])
        # 비어 있지 않으면
        else:
            if stack[-1] == str1[i]:
                stack.pop()
            else:
                stack.append(str1[i])
    print(f'#{tc} {len(stack)}')