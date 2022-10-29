def dfs(i, j):
    global cnt

    visited[i][j] = 1
    cnt += 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and mapp[ni][nj]:
            dfs(ni, nj)
    return

n = int(input())
mapp = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0
ans = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and mapp[i][j]:
            cnt = 0
            dfs(i, j)
            total += 1
            ans.append(cnt)
ans.sort()

print(total)
for z in ans:
    print(z)