def bingo(arr):
    result = 0
    arr_c = list(zip(*arr))
    cnt_ld = 0  # 왼쪽 대각선 검사
    cnt_rd = 0  # 오른쪽 대각선 검사
    for r in range(5):
        if arr[r].count(0) == 5:
            result += 1
        if arr_c[r].count(0) == 5:
            result += 1

        if arr[r][r] == 0:
            cnt_ld += 1
        if arr[r][4-r] == 0:
            cnt_rd += 1

    if cnt_ld == 5:
        result += 1
    if cnt_rd == 5:
        result += 1

    return result

arr = [list(map(int,input().split())) for _ in range(5)]
cnt = 0
ans = []
for tc in range(5):
    ans += list(map(int, input().split()))

for k in range(25):
    for i in range(5):
        if ans[k] in arr[i]:
            arr[i][arr[i].index(ans[k])] = 0
            cnt += 1
            break

    if bingo(arr) > 2:
        print(cnt)
        break