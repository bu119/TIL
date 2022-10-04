di = [-1, 0 ,1, 1, 1, 0, -1, -1] # 우에서 시계
dj = [1, 1, 1, 0, -1, -1, -1, 0]

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    board = [[0]*n for _ in range(n)]
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2
    # print(board)
    b = w = 0
    # 1 흑, 2 백
    for i in range(m):
        c, r, color = map(int, input().split())
        r -= 1
        c -= 1
        board[r][c] = color

        if color == 1:
            target = 2
        else:
            target = 1

        for k in range(8):
            tmp = []
            nr = r + di[k]
            nc = c + dj[k]
            while 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 0:
                    break
                elif board[nr][nc] == target:
                    tmp.append((nr, nc))
                elif board[nr][nc] == color:
                    if tmp:
                        for z in tmp:
                            board[z[0]][z[1]] = color
                    break
                nr += di[k]
                nc += dj[k]


    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                b += 1
            elif board[x][y] == 2:
                w += 1

    print(f'#{tc+1} {b} {w}')