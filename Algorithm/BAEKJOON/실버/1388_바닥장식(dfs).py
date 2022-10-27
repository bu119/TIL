def dfs(i, j, shape):

    if shape == '|':
        for k in [-1, 1]:
            ni = i + k
            if 0 <= ni < n and not visited[ni][j] and pattern[ni][j] == shape:
                visited[ni][j] = 1
                dfs(ni, j, shape)

    else:
        for k in [-1, 1]:
            nj = j + k
            if 0 <= nj < m and not visited[i][nj] and pattern[i][nj] == shape:
                visited[i][nj] = 1
                dfs(i, nj, shape)


n, m = map(int, input().split())
pattern = list(list(input()) for _ in range(n))
visited = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i, j, pattern[i][j])
            cnt += 1
print(cnt)