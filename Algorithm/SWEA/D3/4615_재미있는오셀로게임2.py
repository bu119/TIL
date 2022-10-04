di = [-1, 0, 1, 1, 1, 0, -1, -1]  # 우에서 시계
dj = [1, 1, 1, 0, -1, -1, -1, 0]

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2
    b = w = 0
    # 1 흑, 2 백
    for i in range(m):
        c, r, color = map(int, input().split())
        r -= 1
        c -= 1
        board[r][c] = color
        sr = r
        sc = c
        if color == 1:
            target = 2
        else:
            target = 1

        tmp = []
        k = 0

        while k < 8:

            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc]:
                if board[nr][nc] == target:
                    r = nr
                    c = nc
                    tmp.append((r, c))
                else:
                    if tmp:
                        for z in tmp:
                            board[z[0]][z[1]] = color
                    r = sr
                    c = sc
                    k += 1
                    tmp = []

            else:
                k += 1
                tmp = []
                r = sr
                c = sc

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                b += 1
            elif board[x][y] == 2:
                w += 1

    print(f'#{tc + 1} {b} {w}')