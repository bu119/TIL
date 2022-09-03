# 메모이제이션
memo = [1, 1]
for i in range(2, 31):
    memo.append(memo[i - 1] + 2 * memo[i - 2])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {memo[N // 10]}')