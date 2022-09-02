import sys
sys.stdin = open('testcase/미로_input.txt')

def bfs(x, y):
    global flag
    q = []
    q.append((x, y))             # enQ와 방문체크
    visited[x][y] = 1

    while q:
        x, y = q.pop(0)        # deQ -> 하고픈 일 하기

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스, 벽체크 먼저 하기
            if nx < 0 or nx == 100:
                continue
            if ny < 0 or ny == 100:
                continue

            if arr[nx][ny] == 1:
                continue

            if visited[nx][ny] == 0:
                q.append((nx, ny))  # enQ
                visited[nx][ny] = 1


            if arr[nx][ny] == 3:
                flag = 1
                return

def find_start(arr):
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                return i, j


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, 11):
    flag = 0
    t = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]

    sx, sy = find_start(arr)
    bfs(sx, sy)
    print(f'#{tc} {flag}')