from collections import deque

def bfs(i,j):

    visited[i][j] = 0

    deq = deque()
    deq.append((i, j))
    while deq:
        x, y = deq.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < n:
                total = 1 + visited[x][y]
                if arr[nx][ny] > arr[x][y]:
                    total += arr[nx][ny] - arr[x][y]

                if total < visited[nx][ny]:
                    visited[nx][ny] = total
                    deq.append((nx, ny))

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[1000 * n * 2]*n for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    ans = bfs(0, 0)
    print(f'#{tc+1} {visited[-1][-1]}')