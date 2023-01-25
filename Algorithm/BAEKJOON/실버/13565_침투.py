def bfs(x,y):
    stack = [(x,y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()

        if x == m-1:
            return 'YES'

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx,ny))
    return 'NO'


m, n = map(int, input().split())
arr = [list(map(int, input())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = 'NO'
for i in range(n):
    if arr[0][i] == 0 and visited[0][i] == 0:
        if bfs(0, i) == 'YES':
            ans = 'YES'
            break
print(ans)