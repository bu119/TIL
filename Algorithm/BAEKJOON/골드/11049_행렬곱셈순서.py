import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):  # 현재 대각선 번호
    for j in range(0, n - i):  # 시작 대각선에서 우측 한 칸씩 이동(열)

        if i == 1:  # 시작 행렬의 바로 옆 행렬과 곱
            dp[j][j + i] = matrix[j][0] * matrix[j][1] * matrix[j + i][1]
        else:
            # 바로 옆 행렬 아닐 때
            dp[j][j + i] = 2 ** 31  # 최댓값 넣고 비교
            # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + matrix[j][0] * matrix[k][1] * matrix[j + i][1])

print(dp[0][n-1])