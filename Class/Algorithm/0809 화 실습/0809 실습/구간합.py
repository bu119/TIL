t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    min_a = 10000 * m
    max_a = 0
    for i in range(n-m+1):    # 5-3+1 번 반복
        sum_m = 0
        for j in range(m):    # 3구간씩
            sum_m += a[i+j]   # 1,2,3 / 2,3,4 / 3,4,5

        # 최대 값
        if max_a < sum_m:
            max_a = sum_m
        # 최소 값
        if min_a > sum_m:
            min_a = sum_m

    print(f'#{tc+1} {max_a - min_a}')







