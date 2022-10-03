n = int(input())
find = int(input())
arr = [[0]*n for _ in range(n)]

r = c = n//2

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


arr[r][c] = 1
arr[r-1][c] = 2

num = 2

while num <= n*n:
    num += 1

    for i in