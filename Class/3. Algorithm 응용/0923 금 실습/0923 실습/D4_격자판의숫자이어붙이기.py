def dfs(x, y, k, tmp):
    global memo
    if k == 6:
        memo.add(tmp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, k+1, tmp+str(arr[nx][ny]))


t = int(input())
for tc in range(t):
    arr = [list(map(int,input().split())) for _ in range(4)]
    memo = set()
    dx = [0,1,0,-1] # 우부터 시계
    dy = [1,0,-1,0]

    for x in range(4):
        for y in range(4):
            tmp = str(arr[x][y])
            dfs(x, y, 0, tmp)
    print(f'#{tc+1} {len(memo)}')
    # print(tmp)