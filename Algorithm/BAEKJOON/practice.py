from collections import deque

def bfs(deq):
    global ans

    while deq:
        k, i, j = deq.popleft()

        for d in range(6):
            nk = k + dk[d]
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and box[nk][ni][nj] == 0:
                deq.append((nk, ni, nj))
                box[nk][ni][ni] = box[k][i][i] + 1


m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dk = [1, -1, 0, 0, 0, 0]        # 위 아래 왼쪽 오른쪽 앞 뒤
di = [0, 0, 0, 0, 1, -1]
dj = [0, 0, -1, 1, 0, 0]


deq = deque()
cnt = empty = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                deq.append((k, i, j))
            elif box[k][i][j] == -1:
                empty += 1
            else:
                cnt += 1  # 익지 않은


if cnt + empty == h*n*m:
    print(0)
else:
    bfs(deq)
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if box[k][i][j] == 0:
                    print(-1)
                    exit(0)
    print(ans)
