n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = stairs[1]

if n > 1:                                   # 계단 두개 이상 일 때 (n=1 일 경우 인덱스 에러)
    dp[2] = stairs[1] + stairs[2]

for i in range(3, n+1):                     # 둘 지금, 둘 하나 지금
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

print(dp[n])
# print(dp)