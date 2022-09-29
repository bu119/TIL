def binary(low, high, key, flag):
    if low > high:
        return 0
    else:
        mid = (low+high)//2
        if key == a[mid]:
            return 1
        elif key < a[mid] and flag == 0:            # 이전에 왼쪽이면
            return binary(low, mid - 1, key, 1)
        elif key > a[mid] and flag == 1:            # 이전에 오른쪽이면
            return binary(mid + 1, high, key, 0)
    return 0

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split())) # 정렬
    b = list(map(int, input().split())) # 확인
    a.sort()
    cnt = 0
    flag = 0
    for i in b:
        if binary(0, n-1, i, 0):     # 왼쪽
            cnt += 1
        elif binary(0, n-1, i, 1):   # 오른쪽
            cnt += 1

    print(f'#{tc+1} {cnt}')