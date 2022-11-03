from collections import deque

def bfs(i,j):
    deq = deque()
    deq.append((i, j))
    visited[i][j] = 1   # 방문체크
    w = 1
    while deq:
        i, j = deq.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and picture[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1     # 방문체크
                w += 1
                deq.append((ni, nj))
    return w


n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
maxV = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] and not visited[i][j]:
            cnt += 1
            width = bfs(i, j)
            if maxV < width:
                maxV = width
print(cnt)
print(maxV)