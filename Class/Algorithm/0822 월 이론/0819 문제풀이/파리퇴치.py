import sys; sys.stdin = open('파리퇴치_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_value = 0
            for ii in range(M):
                for jj in range(M):
                    sum_value += arr[i+ii][j+jj]
            if max_value < sum_value:
                max_value = sum_value
    print(f'#{tc} {max_value}')