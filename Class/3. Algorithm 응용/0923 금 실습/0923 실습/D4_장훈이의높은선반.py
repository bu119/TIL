t = int(input())
for tc in range(t):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    ans = 10000 * n

    for i in range(1 << n):
        min_num = 0
        for j in range(n):
            if i & (1 << j):
                min_num += height[j]
            if min_num > ans:
                break
        if b <= min_num and min_num < ans:
            ans = min_num
    print(f'#{tc+1} {ans-b}')