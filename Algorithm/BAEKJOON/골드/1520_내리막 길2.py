import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    if i == m-1 and j == n-1:
        return 1

    if visited[i][j] != -1:     # 방문했으면 경우의 수 가지고 return
        return visited[i][j]

    visited[i][j] = 0           # 방문 체크

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n and rectangle[ni][nj] < rectangle[i][j]:
            visited[i][j] += dfs(ni, nj)    # 4방향 탐색을 통해 끝에서 (i, j)까지 갈 수 있는 경우의 수 더하기

    return visited[i][j]                    # 4방향 탐색이 끝나면 (i, j)에서 갈 수 있는 경우의 수 가지고 재귀를 올라간다.


m, n = map(int, input().split())
rectangle = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(dfs(0, 0))