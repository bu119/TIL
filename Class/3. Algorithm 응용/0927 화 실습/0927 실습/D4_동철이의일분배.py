def dfs(k, pv):
    global ans

    if pv <= ans:           # 소수이므로 곱할수록 작아진다.
        return

    if k == n-1:
        if ans < pv:
            ans = pv
            return
    else:
        for x in range(n):
            if visited[x] == 0:
                visited[x] = 1
                dfs(k+1, pv*p[k+1][x]/100)
                visited[x] = 0

t = int(input())
for tc in range(t):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]

    visited = [0]*n
    ans = 0

    for i in range(n):
        visited[i] = 1
        dfs(0, p[0][i]/100)
        visited[i] = 0

    print(f'#{tc+1} {ans*100:.6f}')