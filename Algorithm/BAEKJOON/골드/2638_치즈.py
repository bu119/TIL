from collections import deque

def bfs(i, j):
    deq = deque()
    deq.append((i, j))
    visited[i][j] = 1

    while deq:
        i, j = deq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if paper[ni][nj]:           # 치즈가 있으면
                    paper[ni][nj] += 1      # 1 더함
                else:
                    visited[ni][nj] = 1     # 치즈가 없으면 방문 체크
                    deq.append((ni, nj))


n, m = map(int, input().split())
paper = [list(map(int,input().split())) for _ in range(n)]

di = [0, 1, 0, -1]  # 우하좌상 탐색
dj = [1, 0, -1, 0]

cnt = 0
flag = 1
while flag:

    flag = 0
    visited = [[0] * m for _ in range(n)]

    bfs(0, 0)
    for x in range(n):
        for y in range(m):
            if paper[x][y] >= 3:
                paper[x][y] = 0
            elif paper[x][y] > 0:
                flag = 1
                paper[x][y] = 1
    cnt += 1

print(cnt)