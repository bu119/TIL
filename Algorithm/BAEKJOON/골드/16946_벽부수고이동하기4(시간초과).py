import sys
input = sys.stdin.readline

def bfs(i,j):
    visited = [[0]*m for _ in range(n)]
    stack = []
    stack.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not mmap[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                stack.append((ni,nj))
    return cnt


n, m = map(int, input().split())
mmap = [list(map(int, input().rstrip())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mmap[i][j] == 1:
            ans[i][j] = bfs(i,j) % 10

for z in ans:
    print(''.join(map(str, z)))