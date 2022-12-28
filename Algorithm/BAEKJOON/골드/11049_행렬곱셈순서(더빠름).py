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

dp = [[0] * (n+1) for _ in range(n+1)]

for k in range(1, n):
    dp[k][k+1] = matrix[k-1] * matrix[k] * matrix[k+1]

for i in range(3, n+1):  # 현재 대각선 시작 번호
    for start in range(1, n - i + 2):  # 시작 대각선에서 우측으로 한 칸씩 이동(열)
        end = start + i - 1
        dp[start][end] = 2 ** 31  # 최댓값 넣고 비교
        # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for mid in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + matrix[start-1] * matrix[mid] * matrix[end])

print(dp[1][n])