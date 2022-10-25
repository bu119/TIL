def line(r, c, cnt):
    global ans
    flag = 1

    if ans and cnt >= ans:
        return

    if r == 5:
        if c == j and ans > cnt:
            ans = cnt
        return

    tmp = []
    for k in [-1, 1]:
        nc = c + k
        if 0 <= nc < h:
            if not visited[r][nc] and ladder[r][nc]:
                visited[r][nc] = 1
                flag = 0
                line(r+1, nc, cnt)
            else:
                tmp.append((r+1, nc))

    if flag:
        visited[r][c] = 1
        line(r + 1, c + 1, cnt)
        for row, col in tmp:
            visited[row][col] = 1
            line(row, col, cnt+1)



n, m, h = map(int, input().split())

ladder = [[0]*n for _ in range(h)]

dr = [0, 0, 1] # 좌 우 아래
dc = [-1, 1, 1]

ans = 0

for i in range(m):
    a, b = map(int, input().split())

    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 1
    for j in range(m):
        visited = [[0] * n for _ in range(h)]
        visited[0][j] = 1
        line(0, j, 0)

if ans > 3:
    print(-1)
print(ans)
print(ladder)