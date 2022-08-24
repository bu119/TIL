import sys
sys.stdin = open('Forth_input.txt')

def operator(a,b,s):
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '*':
        return a * b
    elif s == '/':
        return a // b

t = int(input())
for tc in range(t):
    tmp = input().split()
    print(f'#{tc+1}', end=' ')
    stack = []
    for i in tmp:
        if i.isdigit():
            stack.append(int(i))
        elif i == '.':
            if len(stack) == 1:
                print(stack.pop())
            else:
                print('error')
            break
        elif len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            tmp = operator(b, a, i)
            stack.append(tmp)
        else:
            print('error')
            break
