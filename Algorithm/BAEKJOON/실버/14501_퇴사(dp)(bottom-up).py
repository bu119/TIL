n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

# bottom-up
for i in range(n):
    for j in range(i + schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[n])