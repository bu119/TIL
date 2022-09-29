def dfs(i, j, k, tmp):
    global tmp_memo
    global memo

    if k == 7:
        memo.append(tmp)
        return

    if k >= 2 and [tmp, (i,j)] in tmp_memo:
        return
    elif k >= 2:
        tmp_memo.append([tmp, (i,j)])

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, k+1, tmp+str(arr[ni][nj]))


t = int(input())
for tc in range(t):
    arr = [list(map(int,input().split())) for _ in range(4)]
    memo = []
    tmp_memo = []
    di = [0,1,0,-1] # 우부터 시계
    dj = [1,0,-1,0]

    for i in range(4):
        for j in range(4):
            tmp = str(arr[i][j])
            dfs(i, j, 0, tmp)