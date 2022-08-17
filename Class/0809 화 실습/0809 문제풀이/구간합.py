T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 최대값, 최소값 초기화
    max_value = 0
    min_value = 987654321

    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += arr[i + j]
        # 최대값/최소값 업데이트
        if max_value < total:
            max_value = total
        if min_value > total:
            min_value = total

    print(f'#{tc} {max_value - min_value}')