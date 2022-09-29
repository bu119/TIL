def dfs(x, y, ssum):
    global ans

    if ans < ssum:                      # 가지치기
        return

    if x == N - 1 and y == N - 1:
        if ans > ssum:
            ans = ssum
    else:
        if x + 1 < N:
            dfs(x + 1, y, ssum + arr[x + 1][y])
        if y + 1 < N:
            dfs(x, y + 1, ssum + arr[x][y + 1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0xffffff
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {ans}')