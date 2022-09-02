T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_value = 1000000
    max_value = 0

    for i in range(N):
        if min_value > arr[i]:
            min_value = arr[i]
        if max_value < arr[i]:
            max_value = arr[i]

    print(f'#{tc} {max_value - min_value}')