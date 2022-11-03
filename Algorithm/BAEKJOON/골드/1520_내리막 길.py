import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    global ans

    if i == m-1 and j == n-1:
        ans += 1
        return 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n and rectangle[ni][nj] < rectangle[i][j]:
            if visited[ni][nj]:
                ans += 1
                return 1

            visited[ni][nj] += dfs(ni, nj)
    return 0


m, n = map(int, input().split())
rectangle = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ans = 0
dfs(0, 0)
print(ans)

