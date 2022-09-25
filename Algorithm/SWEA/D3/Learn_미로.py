def dfs(x, y):
    global flag

    if maze[x][y] == 3:
        flag = 1
        return

    if flag:
        return

    visited[x][y] = 1

    for z in range(4):
        nx = x + di[z]
        ny = y + dj[z]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and maze[nx][ny] != 1:
            dfs(nx, ny)

t = int(input())
for tc in range(t):
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visited = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n-1,-1,-1):
        for j in range(n):
            if maze[i][j] == 2:
                dfs(i,j)
                break
    print(f'#{tc+1} {flag}')