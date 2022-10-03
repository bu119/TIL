t = int(input())
for tc in range(t):
    n = int(input())

    arr = [[0]*n for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    num = 1
    i = j = k = 0
    arr[i][j] = num

    while num < n*n:

        i += di[k]
        j += dj[k]
        if 0 <= i < n and 0 <= j < n and arr[i][j] == 0:
            num += 1
            arr[i][j] = num
        else:
            i -= di[k]
            j -= dj[k]
            k = (k+1) % 4

    print(f'#{tc+1}')
    for x in arr:
        print(' '.join(map(str, x)))