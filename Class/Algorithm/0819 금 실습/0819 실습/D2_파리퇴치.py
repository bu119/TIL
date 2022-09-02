import sys
sys.stdin = open("파리_input.txt", "r")

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_m = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for row in range(m):
                for col in range(m):
                    total += arr[i+row][j+col]
            if max_m < total:
                max_m = total
    print(f'#{tc+1} {max_m}')
