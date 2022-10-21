from collections import deque

def bfs(y, x):
    width = 1
    deq = deque()
    deq.append((y, x))

    visited[y][x] = 1
    paper[y][x] = 1

    while deq:
        y, x = deq.popleft()
        for u in range(4):
            ny = y + dj[u]
            nx = x + di[u]
            if 0 <= ny < m and 0 <= nx < n and not paper[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                paper[ny][nx] = 1
                deq.append((ny, nx))
                width += 1
    return width


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
            w.append(bfs(y, x))

print(cnt)
w.sort()

for v in w:
    print(v, end=' ')