def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def dfs(x, y):
    global flag
    if arr[x][y] == 3:
        flag = 1
        return

    # 방문체크
    visited[x][y] = 1
    # 인접한 정점이 방문 안 했으면 dfs
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스, 방문체크, 벽체크
        if nx < 0 or nx == N: continue
        if ny < 0 or ny == N: continue
        if visited[nx][ny] == 1: continue
        if arr[nx][ny] == 1: continue
        dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    flag = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    sx, sy = find_start(arr)
    dfs(sx, sy)
    print(f'#{tc} {flag}')