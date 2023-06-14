import sys
input = sys.stdin.readline

dp = [0] * 1000001
dp[1], dp[2], dp[3], dp[4] = 1, 2, 4, 7
for i in range(5, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
