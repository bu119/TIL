import sys
sys.stdin = open('testcase/input_보급로.txt')

from collections import deque

def bfs(x, y):
    deq = deque()
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < n and not(nx == 0 and ny == 0):
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    deq.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        deq.append((nx, ny))

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    time = [[0]*n for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    bfs(0, 0)

    print(f'#{tc+1} {time[-1][-1]}')
