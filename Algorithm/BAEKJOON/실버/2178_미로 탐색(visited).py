from collections import deque

def bfs(i,j):
    deq = deque()
    deq.append((i, j))
    visited[i][j] = 1

    while deq:
        i, j = deq.popleft()

        if i == n-1 and j == m-1:
            return visited[i][j]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and miro[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                deq.append((ni,nj))


n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(bfs(0,0))