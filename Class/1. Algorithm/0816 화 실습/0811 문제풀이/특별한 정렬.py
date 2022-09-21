def selection_sort(a, n):
    for i in range(10):
        idx = i
        if i % 2 == 0:
            # 최대값
            for j in range(i + 1, n):
                if a[idx] < a[j]:
                    idx = j
        else:
            # 최소값
            for j in range(i + 1, n):
                if a[idx] > a[j]:
                    idx = j
        # 바꾸기
        arr[i], arr[idx] = arr[idx], arr[i]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, n)

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()