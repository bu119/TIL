import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    global width
    if 0 <= i < n and 0 <= j < m and picture[i][j]:
        picture[i][j] = 0
        width += 1

        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i-1, j)

    else:
        return


n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

maxV = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if picture[i][j]:
            width = 0
            cnt += 1
            dfs(i, j)
            if maxV < width:
                maxV = width
print(cnt)
print(maxV)