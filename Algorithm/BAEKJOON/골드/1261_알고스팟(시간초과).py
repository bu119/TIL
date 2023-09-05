import sys
input = sys.stdin.readline

def dfs(i,j, cnt):
    global ans

    if cnt > ans:
        return

    if i == n-1 and j == m-1:
        ans = min(ans, cnt)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = 1

            if board[ni][nj] == '0':
                dfs(ni, nj, cnt)
            else:
                dfs(ni, nj, cnt + 1)

            visited[ni][nj] = 0


m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 10001

di = [0,1,0,-1]
dj = [1,0,-1,0]

dfs(0,0,0)
print(ans)