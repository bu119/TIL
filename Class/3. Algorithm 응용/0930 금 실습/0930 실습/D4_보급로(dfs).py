import sys
sys.stdin = open('testcase/input_보급로.txt')

def dfs(x, y, ssum):
    global ans

    if ans <= ssum:
        return

    if x == y == n-1 and ssum < ans:
        ans = ssum
        return

    visited[x][y] = 1

    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            dfs(nx, ny, ssum + arr[nx][ny])
            visited[nx][ny] = 0

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    ans = 10000
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    dfs(0, 0, arr[0][0])

    print(ans)