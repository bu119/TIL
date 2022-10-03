t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0
    for r in range(n-m+1):
        for c in range(n - m + 1):
            tmp_v = 0
            for i in range(m):
                for j in range(m):
                    tmp_v += arr[i+r][j+c]
            if max_v < tmp_v:
                max_v = tmp_v
    print(f'#{tc+1} {max_v}')
