import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
ans = 1000000
for i in range(3):
    dp = [[1000, 1000, 1000] for _ in range(n)]
    # 첫 집 설정
    dp[0][i] = house[0][i]
    for j in range(1, n):
        dp[j][0] = house[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = house[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = house[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    # 첫 집과 마지막 집의 색이 다름
    for k in range(3):
        if i != k:
            ans = min(ans, dp[n-1][k])
print(ans)