import sys
sys.stdin = open('input_단순이진암호.txt')

secret = {(0,0,0,1,1,0,1): 0, (0,0,1,1,0,0,1): 1, (0,0,1,0,0,1,1): 2, (0,1,1,1,1,0,1): 3, (0,1,0,0,0,1,1): 4, (0,1,1,0,0,0,1): 5, (0,1,0,1,1,1,1): 6, (0,1,1,1,0,1,1): 7, (0,1,1,0,1,1,1): 8, (0,0,0,1,0,1,1): 9}

t = int(input())
for tc in range(t):
    n, m = map(int,input().split())
    arr = [list(map(int, input())) for _ in range(n)]

    x = 0
    ans = 0
    judge = 0

    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j]:
                x, y = i, j
                break
        if x:
            break

    code = arr[x][y - 55:y + 1]
    for z in range(1, 9):
        tmp = tuple(code[7*(z-1):7*z])
        ans += secret[tmp]
        if z % 2:
            judge += secret[tmp] * 3
        else:
            judge += secret[tmp]

    if judge % 10:
        print(f'#{tc + 1} 0')
    else:
        print(f'#{tc+1} {ans}')