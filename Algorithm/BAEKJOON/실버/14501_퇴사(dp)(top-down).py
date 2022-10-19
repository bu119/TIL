n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

# top-down
for i in range(n-1, -1, -1):
    if i + schedule[i][0] <= n:  # 퇴사 날 전까지 (일 안하고 한거 비교)
        dp[i] = max(dp[i+1], dp[i + schedule[i][0]] + schedule[i][1])
    else:                       # 퇴사 날 넘음 (일 안함)
        dp[i] = dp[i + 1]

print(dp[0])