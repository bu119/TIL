t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # 집: H, 기지국: A-1, B-2, C-3
    cover = {'A': 1, 'B': 2, 'C': 3}

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    cnt = 0
    for i in range(n):
        for j in range(n):

            if arr[i][j] in cover:
                for c in range(1, cover[arr[i][j]]+1):
                    for k in range(4):
                        ni = i + di[k] * c
                        nj = j + dj[k] * c
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc+1} {cnt}')