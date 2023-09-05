import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):

    deq = deque()
    deq.append((i,j))
    visited[i][j] = 0

    while deq:
        i, j = deq.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:

                if board[ni][nj] == '0':
                    visited[ni][nj] = visited[i][j]
                    deq.appendleft((ni, nj))
                else:
                    visited[ni][nj] = visited[i][j]+1
                    deq.append((ni, nj))

    return visited[n-1][m-1]


m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

print(bfs(0,0))