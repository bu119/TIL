import sys
input = sys.stdin.readline

n = int(input())
matrix = []

r, c = map(int, input().split())
matrix.append(r)
matrix.append(c)

for _ in range(n-1):
    r, c = map(int, input().split())
    matrix.append(c)

dp = [[0] * n for _ in range(n)]

for i in range(1, n):  # 현재 대각선 시작 번호
    for j in range(0, n - i):  # 시작 대각선에서 우측으로 한 칸씩 이동(열)
        # j 시작 행렬, j+i 끝 행렬
        dp[j][j + i] = 2 ** 31  # 최댓값 넣고 비교
        # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + matrix[j-1] * matrix[k] * matrix[j + i])

print(dp[0][n-1])