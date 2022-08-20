def solve(str1):
    stack = []
    # 문자열 순회
    for i in range(len(str1)):
        # 여는 괄호일 때
        if str1[i] == '(' or str1[i] == '{':
            stack.append(str1[i])
        # 닫는 괄호일 때
        elif str1[i] == ')' or str1[i] == '}':
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop()
            # 같은 쌍인지 검사
            if str1[i] == ')' and tmp != '(':
                return 0
            elif str1[i] == '}' and tmp != '{':
                return 0
    # 스택이 비어있는지 확인
    if stack:
        return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    print(f'#{tc} {solve(str1)}')