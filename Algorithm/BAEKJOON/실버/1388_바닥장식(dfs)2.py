def dfs(i, j):

    if pattern[i][j] == '|':
        for k in [-1, 1]:
            ni = i + k
            if 0 <= ni < n and not visited[ni][j] and pattern[ni][j] == '|':
                visited[ni][j] = 1
                dfs(ni, j)

    else:
        for k in [-1, 1]:
            nj = j + k
            if 0 <= nj < m and not visited[i][nj] and pattern[i][nj] == '-':
                visited[i][nj] = 1
                dfs(i, nj)


n, m = map(int, input().split())
pattern = list(list(input()) for _ in range(n))
visited = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i, j)
            cnt += 1
print(cnt)