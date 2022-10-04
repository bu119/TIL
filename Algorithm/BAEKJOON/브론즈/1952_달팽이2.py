m, n = map(int, input().split())

arr = [[0]*n for _ in range(m)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

num = n*m

i = j = k = cnt = 0
arr[i][j] = 1

while num > 1:

    i += di[k]
    j += dj[k]
    if 0 <= i < m and 0 <= j < n and not arr[i][j]:
        arr[i][j] = 1
        num -= 1
    else:
        i -= di[k]
        j -= dj[k]
        k = (k+1) % 4
        cnt += 1

print(cnt)