import sys
sys.setrecursionlimit(1000000)

def dfs(y, x):
    global width
    width += 1

    visited[y][x] = 1
    paper[y][x] = 1

    for u in range(4):
        ny = y + dj[u]
        nx = x + di[u]
        if 0 <= ny < m and 0 <= nx < n and not paper[ny][nx] and not visited[ny][nx]:
            dfs(ny, nx)


m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]

dj = [0, 1, 0, -1]
di = [1, 0, -1, 0]

w = []
cnt = 0
# 그림상 좌표는 밑에서 부터 시작하지만 결과적으로 같은 그림
for z in range(k):
    dx, dy, ux, uy = map(int, input().split())
    for i in range(dy, uy):
        for j in range(dx, ux):
            paper[i][j] = 1

visited = [[0] * n for _ in range(m)]
for y in range(m):
    for x in range(n):
        if paper[y][x] == 0:
            cnt += 1
            width = 0
            dfs(y, x)
            w.append(width)

print(cnt)
w.sort()

for v in w:
    print(v, end=' ')
