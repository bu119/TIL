import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ssum = [[0]*n for _ in range(n)] # 누적 합

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            ssum[i][j] = arr[i][j]
        elif i == 0:
            ssum[i][j] = arr[i][j] + ssum[i][j - 1]
        elif j == 0:
            ssum[i][j] = arr[i][j] + ssum[i - 1][j]
        else:
            ssum[i][j] = ssum[i][j-1] + ssum[i-1][j] + arr[i][j] - ssum[i-1][j-1]
# print(ssum)
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1-1 == 0 and y1-1 == 0:
        ans = ssum[x2-1][y2-1]
    elif x1-1 == 0:
        ans = ssum[x2-1][y2-1] - ssum[x2-1][y1-2]
    elif y1-1 == 0:
        ans = ssum[x2 - 1][y2 - 1] - ssum[x1 - 2][y2 - 1]
    else:
        ans = ssum[x2-1][y2-1] - ssum[x2-1][y1-2] - ssum[x1-2][y2-1] + ssum[x1-2][y1-2]
    print(ans)