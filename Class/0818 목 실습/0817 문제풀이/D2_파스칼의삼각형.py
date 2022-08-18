size = 100
memo = [[0] * 100 for _ in range(size)]

for i in range(size):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    print(f'#{tc}')

    for i in range(n):
        for j in range(i+1):
            print(memo[i][j], end=' ')
        print()