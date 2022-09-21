import time
start = time.time()                              # 시간 탐색

import sys
sys.stdin = open('testcase/input_정사각형방.txt')

from collections import deque

def bfs(i, j):
    deq = deque()
    deq.append((i, j))
    visited[i][j] = 1
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == arr[x][y] + 1:
                visited[ni][nj] = visited[x][y] + 1
                deq.append((ni, nj))
    return visited[x][y]

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]
    di = [0, 1, 0, -1]  # 우 부터 시계방향
    dj = [1, 0, -1, 0]
    max_cnt = 0

    for i in range(n):
        for j in range(n):
            cnt = bfs(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                ans = arr[i][j]
            elif max_cnt == cnt and ans > arr[i][j]:
                ans = arr[i][j]
    print(f'#{tc + 1} {ans} {max_cnt}')

print(time.time() - start)