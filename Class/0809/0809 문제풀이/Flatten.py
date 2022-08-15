T = 10
for tc in range(1, T+1):
    dump_count = int(input())
    N = 100
    arr = list(map(int, input().split()))

    for i in range(dump_count):
        # 최소/최대값의 인덱스
        max_idx = min_idx = 0
        for j in range(1, N):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[max_idx] -= 1
        arr[min_idx] += 1

        # 반드시 최종덤프후에 최고점과 최저점의 높이차를 반환
        max_idx = min_idx = 0
        for j in range(1, N):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j

    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')