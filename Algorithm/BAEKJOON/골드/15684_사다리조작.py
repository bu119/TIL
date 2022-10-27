import sys
input = sys.stdin.readline

def linenum():
    for start in range(n):  # 세로 줄 선택
        line = start
        for i in range(h):  # 가로
            if ladder[i][line]:
                line += 1
            elif ladder[i][line - 1]:
                line -= 1
        if line != start:
            return 0
    return 1


def dfs(row, col, cnt):
    global ans

    if cnt >= ans or cnt > 3:
        return

    if linenum():
        if ans > cnt:
            ans = cnt
        return

    for r in range(row, h):   # 행 (가로 선)
        if r == row:
            k = col
        else:
            k = 0
        for j in range(k, n-1): # 열 (세로 선)
            if not ladder[r][j] and not ladder[r][j+1] and not ladder[r][j-1]:
                ladder[r][j] = 1
                dfs(r, j, cnt+1)
                ladder[r][j] = 0


n, m, h = map(int, input().split())
ladder = [[0]*n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

ans = 4

dfs(0, 0, 0)

if ans > 3:
    ans = -1

print(ans)