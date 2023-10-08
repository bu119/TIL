# 스티커 한 장을 떼면
# 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
# 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    if n > 1:
        # 2 개일 때는 지그재그가 최대
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    # 2 이상 일 때는 한 칸 건너뛰기 가능
    for i in range(2, n):
        # 계속 지그재그로 가는 경우와 한칸을 건너뛰는 경우를 비교
        dp[0][i] += max(dp[1][i - 1],  dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1],  dp[0][i - 2])

    print(max(dp[0][n-1], dp[1][n-1]))