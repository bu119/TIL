k = int(input())
arr = [tuple(map(int, input().split())) for _ in range(6)]
minus = 1
max_r = 0
max_c = 0
for i in range(6):

    if arr[i-2][0] == arr[i][0]:          # 작은 사각형의 변은 큰 사각형의 같은 방향 사이에 존재
        minus *= arr[i-1][1]
        # print(arr[i][1])
        # print(minus)

    if arr[i][0] == 1 or arr[i][0] == 2:        # 동서 방향에서 큰 변 찾기
        if arr[i][1] > max_c:
            max_c = arr[i][1]
            # print(max_c)
    elif arr[i][0] == 3 or arr[i][0] == 4:      # 남북 방향에서 큰 변 찾기
        if arr[i][1] > max_r:
            max_r = arr[i][1]
            # print(max_r)

ans = (max_c * max_r - minus) * k
print(ans)