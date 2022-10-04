def perm(k, ssum):
    global ans
    if ans <= ssum:
        return

    if k == n-1:
        if ssum < ans:
            ans = ssum
    else:
        for x in range(n):
            if not visited[x]:
                visited[x] = 1
                perm(k+1, ssum+arr[k+1][x])
                visited[x] = 0

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 10*n
    for i in range(n):
        visited[i] = 1
        perm(0, arr[0][i])
        visited[i] = 0

    print(f'#{tc+1} {ans}')