import sys
input = sys.stdin.readline

def bfs(i, j, alpha):
    global ans

    stack = [(i, j, alpha)]
    visited[i][j] = board[i][j]

    while stack:
        i, j, alpha = stack.pop()

        if ans < len(alpha):
            ans = len(alpha)

        if ans == 26:
            return

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < r and 0 <= nj < c and board[ni][nj] not in alpha:
                check = alpha + board[ni][nj]
                if visited[ni][nj] != check:
                    visited[ni][nj] = check
                    stack.append((ni, nj, check))


r, c = map(int,input().split())
board = [list(input()) for _ in range(r)]
visited = [[''] * c for _ in range(r)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

ans = 0
bfs(0, 0, board[0][0])

print(ans)