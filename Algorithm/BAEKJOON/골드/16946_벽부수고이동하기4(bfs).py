import sys
input = sys.stdin.readline

def bfs(i,j):
    wall = set()
    stack = []
    stack.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if not mmap[ni][nj]:
                    visited[ni][nj] = 1
                    cnt += 1
                    stack.append((ni,nj))
                else:
                    wall.add((ni,nj))

    for x, y in wall:
        mmap[x][y] += cnt
        # 나머지가 0이 될 수 있으므로 틀린다.
        # mmap[x][y] = (mmap[x][y] + cnt) % 10


n, m = map(int, input().split())
mmap = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if not mmap[i][j] and not visited[i][j]:
            bfs(i, j)

for r in range(n):
    for c in range(m):
        print(mmap[r][c] % 10, end='')
    print()