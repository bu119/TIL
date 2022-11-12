import sys
input = sys.stdin.readline

def dfs(i, j, k):
    global cnt

    if i == n-1 and j == n-1:
        cnt += 1
        return

    ni = i + 1
    nj = j + 1
    # 가로
    if k == 'g' or k == 'd':
        if nj < n and not house[i][nj]:
            dfs(i, nj, 'g')
    # 세로
    if k == 's' or k == 'd':
        if ni < n and not house[ni][j]:
            dfs(ni, j, 's')
    # 대각선
    if ni < n and nj < n and not house[ni][nj] and not house[i][nj] and not house[ni][j]:
        dfs(ni, nj, 'd')


n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
dfs(0, 1, 'g')

print(cnt)