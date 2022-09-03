import sys
sys.stdin = open('testcase/기지국_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    space = [list(input()) for _ in range(n)]

    di = [0, 0, 1, -1]      # 동서남북
    dj = [1, -1, 0, 0]
    cnt = 0
    cover = {'A': 1, 'B': 2, 'C': 3}

    for i in range(n):
        for j in range(n):
            if space[i][j] in cover:
                for ch in range(1, cover[space[i][j]] + 1):    # 'C'이면 1,2,3 탐색
                    for k in range(4):
                        ci = i + di[k] * ch
                        cj = j + dj[k] * ch
                        if 0 <= ci < n and 0 <= cj < n:        # 벽 체크
                            if space[ci][cj] == 'H':           # H가 있으면
                                space[ci][cj] = 'X'            # X로 변경

    for i in range(n):
        for j in range(n):
            if space[i][j] == 'H':
                cnt += 1

    print(f'#{tc+1} {cnt}')
