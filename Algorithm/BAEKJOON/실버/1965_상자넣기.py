n = int(input())
box = list(map(int, input().split()))

num = max(box)
dp = [0] * (num + 1)    # 가장 큰 상자 크기 만큼 만들어주기

dp[box[0]] = 1
for i in range(1, n):
    dp[box[i]] = max(dp[:box[i]]) + 1   # 작은 상자 중 많은 개수에 +1

print(max(dp))  # 가장 많은 개수 구하기

