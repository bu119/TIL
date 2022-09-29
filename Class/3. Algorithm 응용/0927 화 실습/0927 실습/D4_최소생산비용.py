def dfs(k, ssum):           # k는 깊이
    global visited
    global ans

    if k == (n-1) and ans >= ssum:
        ans = ssum
        return

    if ans < ssum:
        return
    else:
        for x in range(n):
            if visited[x] == 0:
                visited[x] = 1
                dfs(k+1, ssum+cost[k+1][x])
                visited[x] = 0

t = int(input())
for tc in range(t):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n
    ans = 99*n
    for i in range(n):
        visited[i] = 1
        dfs(0, cost[0][i])
        visited[i] = 0

    print(f'#{tc+1} {ans}')
