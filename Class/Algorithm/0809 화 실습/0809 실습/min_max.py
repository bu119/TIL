t = int(input())
for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_a = a[0]            # 최소값
    for i in range(n):
        if min_a > a[i]:
            min_a = a[i]
    max_a = 0
    for j in range(n):     # 최대값
        if max_a < a[j]:
            max_a = a[j]

    print(f'#{tc + 1} {max_a - min_a}')
