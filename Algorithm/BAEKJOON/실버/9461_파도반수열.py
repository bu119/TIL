dp = [0] * 101
dp[1] = dp[2] = 1
for i in range(3, 101):
    dp[i] = dp[i-3] + dp[i-2]

t = int(input())
for tc in range(t):
    n = int(input())
    print(dp[n])