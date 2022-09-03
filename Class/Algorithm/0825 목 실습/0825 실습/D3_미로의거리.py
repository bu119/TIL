import sys
sys.stdin = open('testcase/미로의거리_input.txt')

def bfs(x, y):
    global flag
    q = []
    q.append((x, y))             # enQ와 방문체크
    visited[x][y] = 1
    global cnt

    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스, 벽체크 먼저 하기
            if nx < 0 or nx == N:
                continue
            if ny < 0 or ny == N:
                continue

            if arr[nx][ny] == 1:
                continue

            if visited[nx][ny] == 0:
                q.append((nx, ny))  # enQ
                visited[nx][ny] = 1
                cnt += 1
            else:
                cnt -= 1



            if arr[nx][ny] == 3:
                flag = 1
                return

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    flag = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    sx, sy = find_start(arr)
    bfs(sx, sy)
    print(f'#{tc} {cnt}')
