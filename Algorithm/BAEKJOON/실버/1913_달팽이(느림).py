n = int(input())
target = int(input())
arr = [[0]*n for _ in range(n)]

di = [1, 0, -1, 0]  # 하 우 상 좌
dj = [0, 1, 0, -1]

num = n**2
i = j = k = r = c = 0
arr[i][j] = num

while num > 1:
    ni = i + di[k]
    nj = j + dj[k]
    if 0 <= ni < n and 0 <= nj < n and not arr[ni][nj]:
        num -= 1
        i = ni
        j = nj
        arr[i][j] = num
        if num == target:
            r = i
            c = j
    else:
        k = (k+1) % 4

for x in arr:
    print(*x)
print(r+1, c+1)