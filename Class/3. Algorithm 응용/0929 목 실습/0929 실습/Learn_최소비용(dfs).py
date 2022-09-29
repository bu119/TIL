def dfs(i, j, ssum):
    global ans

    if ans <= ssum:
        return

    if i == n-1 and j == n-1 and ssum < ans:
        ans = ssum
        return

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, ssum+1+(arr[ni][nj]-arr[i][j]))
            visited[ni][nj] = 0

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    di = [0, 1]
    dj = [1, 0]

    ans = 1000 * n * 2

    visited[0][0] = 1
    dfs(0, 0, arr[0][0])
    print(f'#{tc+1} {ans}')