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

        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            num += 1
            i = ni
            j = nj
            arr[i][j] = num
        else:
            k = (k+1) % 4

    print(f'#{tc+1}')
    for x in arr:
        print(' '.join(map(str, x)))