n, m, h = map(int, input().split())

ladder = [[0]*n for _ in range(h)]

for i in range(m):
    a, b = map(int, input().split())

    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 1

print(ladder)