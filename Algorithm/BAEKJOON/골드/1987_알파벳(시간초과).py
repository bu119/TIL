import sys
input = sys.stdin.readline

def dfs(i, j, cnt):
    global ans

    if ans < cnt:
        ans = cnt

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < r and 0 <= nj < c:
            if board[ni][nj] not in check:
                check.add(board[ni][nj])
                dfs(ni, nj, cnt+1)
                check.remove(board[ni][nj])

r, c = map(int,input().split())
board = [list(input()) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

ans = 0
# 알파벳 자체가 방문 체크 해줌
check = set(board[0][0])
dfs(0, 0, 1)

print(ans)