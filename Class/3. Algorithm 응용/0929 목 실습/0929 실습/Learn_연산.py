def dfs(n, cnt):
    global ans

    if ans <= cnt:
        return

    if n == m:
        if cnt < ans:
            ans = cnt
        return

    for x in range(4):
        if x == 0:
            num = n + 1
        elif x == 1:
            num = n - 1
        elif x == 2:
            num = n * 2
        else:
            num = n - 10

        dfs(num, cnt+1)

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    ans = 1000001
    dfs(n, 0)
    print(f'#{tc+1} {ans}')