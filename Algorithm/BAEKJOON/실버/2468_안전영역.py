import sys
input = sys.stdin.readline

def bfs(i,j):
    stack = [(i, j)]
    visited[i][j] = 1

    while stack:
        i, j = stack.pop()

        for z in range(4):
            ni = i + di[z]
            nj = j + dj[z]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > k and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                stack.append((ni,nj))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = 0
num = [0]
for i in range(n):
    for j in range(n):
        if arr[i][j] not in num:
            num.append(arr[i][j])

for k in num:
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                cnt += 1
                bfs(i, j)
    if ans < cnt:
        ans = cnt

print(ans)