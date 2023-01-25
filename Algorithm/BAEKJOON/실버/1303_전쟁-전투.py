def bfs(i,j,color):
    stack = [(i,j)]
    visited[i][j] = 1
    cnt = 1
    while stack:
        i,j = stack.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < m and 0 <= nj < n and soldier[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                stack.append((ni,nj))
    return cnt


n, m = map(int, input().split())
soldier = [list(input()) for _ in range(m)]

visited = [[0]*n for _ in range(m)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

w_cnt = 0
b_cnt = 0

for i in range(m):
    for j in range(n):
        if soldier[i][j] == 'W' and not visited[i][j]:
            cnt = bfs(i,j,'W')
            w_cnt += (cnt*cnt)
        if soldier[i][j] == 'B' and not visited[i][j]:
            cnt = bfs(i,j,'B')
            b_cnt += (cnt*cnt)

print(w_cnt, b_cnt)