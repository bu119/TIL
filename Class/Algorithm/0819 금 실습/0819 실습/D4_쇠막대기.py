import sys
sys.stdin=open('막대기_input.txt')

t = int(input())
for tc in range(t):
    stick = input()
    top = 0
    cnt = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            top += 1
        if stick[i] == ')':
            top -= 1
            if stick[i-1] == '(':
                cnt += top
            else:
                cnt += 1
    print(f'#{tc+1} {cnt}')



