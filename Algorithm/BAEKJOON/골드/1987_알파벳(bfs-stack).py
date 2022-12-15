import sys
input = sys.stdin.readline

def bfs(i, j, alpha):
    global ans

    stack = [(0, 0, board[0][0])]

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
                stack.append((ni, nj, alpha + board[ni][nj]))

r, c = map(int,input().split())
board = [list(input()) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

ans = 0
bfs(0, 0, board[0][0])

print(ans)