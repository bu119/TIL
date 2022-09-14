import sys
sys.setrecursionlimit(100000)

def dfs(i, j):                         # 일반인
    visited[i][j] = 1                  # 방문체크

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == color and visited[ni][nj] == 0:
            dfs(ni, nj)

def dfsRG(i, j):                     # 적록색약
    visitedRG[i][j] = 1              # 방문체크

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if color == 'B':
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'B' and visitedRG[ni][nj] == 0:
                dfsRG(ni, nj)
        else:
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 'B' and visitedRG[ni][nj] == 0:
                dfsRG(ni, nj)

n = int(input())
arr = [list(input()) for _ in range(n)]

visited = [[0]*n for _ in range(n)]             # 일반인 방문체크
visitedRG = [[0]*n for _ in range(n)]           # 적록색약 방문체크
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
cnt = 0
cntRG = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:      # 일반인 탐색
            cnt += 1
            color = arr[i][j]
            dfs(i, j)

        if visitedRG[i][j] == 0:    # 적록색약 탐색
            cntRG += 1
            color = arr[i][j]
            dfsRG(i, j)

print(cnt, cntRG)