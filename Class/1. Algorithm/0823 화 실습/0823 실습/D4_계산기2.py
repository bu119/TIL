import sys
sys.stdin = open('계산기2_input.txt')

def change(arr):
    f_operator = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    l_operator = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    stack = []
    result = ''
    for i in range(len(arr)):
        if arr[i] in '+-*/()':
            if not stack:
                stack.append(arr[i])
            else:
                if arr[i] == ')':
                    while stack[-1] != '(':
                        result += stack.pop() # 사이에 연산 result에 넣기
                    stack.pop()  # '(' 버리기
                else:
                    while stack and f_operator[stack[-1]] >= l_operator[arr[i]]:
                        result += stack.pop()
                    stack.append(arr[i])
        else:
            result += arr[i]
    # 스택에 남아있는 연산자 result에 넣기
    while stack:
        result += stack.pop()

    return result

def operator(a,b,s):
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '*':
        return a * b
    elif s == '/':
        return a // b

for tc in range(10):
    n = int(input())
    arr = input()
    new_arr = change(arr)

    stack2 = []
    for i in new_arr:
        if i.isdigit():
            stack2.append(int(i))
        elif len(stack2) > 1:
            a = stack2.pop()
            b = stack2.pop()
            tmp = operator(b, a, i)
            stack2.append(tmp)
    print(f'#{tc+1} {stack2.pop()}')
