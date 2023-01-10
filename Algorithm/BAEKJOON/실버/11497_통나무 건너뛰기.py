t = int(input())
for tc in range(t):
    n = int(input())
    log = list(map(int, input().split()))
    log.sort()
    arr = [0]*n
    for i in range(n):
        idx = i//2
        if i % 2 == 0:
            arr[idx] = log[i]
        else:
            arr[n-1-idx] = log[i]

    dif = 0
    for j in range(n):
        num = abs(arr[j-1]-arr[j])
        if dif < num:
            dif = num
    print(dif)