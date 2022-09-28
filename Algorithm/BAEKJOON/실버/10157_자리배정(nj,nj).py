c, r = map(int, input().split())
k = int(input())

hall = [[0]*c for _ in range(r)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

num = 1
i = r-1
j = 0
z = 0
hall[r-1][0] = 1          # 초기 값

if c*r < k:
    print(0)
else:
    while num < k:

        ni = i + di[z]
        nj = j + dj[z]

        if 0 <= ni < r and 0 <= nj < c and not hall[ni][nj]:
            i, j = ni, nj
            num += 1
            hall[i][j] = num
        else:
            z = (z + 1) % 4

    print(j+1, r-i)       # 출력 값 주의
