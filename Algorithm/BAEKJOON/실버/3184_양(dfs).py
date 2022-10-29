import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    global sheep
    global wolf

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == 0 and yard[ni][nj] != '#':
            visited[ni][nj] = 1
            if yard[ni][nj] == 'v':
                wolf += 1
            if yard[ni][nj] == 'o':
                sheep += 1

            dfs(ni, nj)


r, c = map(int, input().split())
yard = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

livesheep = 0
livewolf = 0
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            sheep = 0
            wolf = 0
            visited[i][j] = 1
            dfs(i,j)
            if sheep > wolf:
                livesheep += sheep
            else:
                livewolf += wolf

print(livesheep, livewolf)
