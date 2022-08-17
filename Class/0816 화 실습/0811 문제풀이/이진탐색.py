def binary_search(arr, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end) // 2
        if key == arr[middle]:
            return cnt
        elif key < arr[middle]:
            end = middle
        else:
            start = middle
    # return False


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P + 1))

    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)

    ans = '0'
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'

    print(f'#{tc} {ans}')