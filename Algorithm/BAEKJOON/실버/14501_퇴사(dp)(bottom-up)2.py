n = int(input())
schedule = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+2)

# bottom-up
for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[i])
    if i + schedule[i][0] <= n:   # 퇴사 날까지
        dp[i + schedule[i][0]] = max(dp[i + schedule[i][0]], dp[i] + schedule[i][1])

dp[n+1] = max(dp[n+1], dp[n])
print(dp[n+1])

# print(dp)