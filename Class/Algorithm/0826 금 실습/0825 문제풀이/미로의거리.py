import sys; sys.stdin = open('미로의거리_input.txt')

def find_start(arr):
    #출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(x, y):
    Q = []
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :  # 인덱스 체크
                if arr[nx][ny] == 3:
                    return visited[x][y] - 1
                elif arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    x, y = find_start(arr)
    print(f'#{tc} {bfs(x, y)}')

