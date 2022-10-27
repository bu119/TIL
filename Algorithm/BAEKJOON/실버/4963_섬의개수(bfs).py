from collections import deque

def bfs(i, j):
    deq = deque()
    deq.append((i, j))

    visited[i][j] = 1

    while deq:
        i, j = deq.popleft()

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and mapp[ni][nj]:
                visited[ni][nj] = 1
                deq.append((ni, nj))


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    mapp = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, -1, 1]

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and mapp[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
