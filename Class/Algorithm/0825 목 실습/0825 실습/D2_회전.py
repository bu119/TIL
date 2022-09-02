import sys
sys.stdin = open('testcase/회전_input.txt')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    for i in range(m):
        num.append(num.pop(0))
    print(f'#{tc+1} {num[0]}')