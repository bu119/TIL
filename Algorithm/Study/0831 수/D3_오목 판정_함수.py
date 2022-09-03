import sys
sys.stdin = open('testcase/오목_mine.txt')

def judge(arr):
    arr_col = list(zip(*arr))
    cnt_l = 0
    cnt_r = 0
    for r in range(5):
        # 행 탐색
        if arr[r].count('o') == 5:
            return 1
        # 열 탐색
        if arr_col[r].count('o') == 5:
            return 1
        # 대각선
        if arr[r][r] == 'o':
            cnt_l += 1

        if arr[r][4-r] == 'o':
            cnt_r += 1

        # 대각선 오목 탐색
    if cnt_l == 5 or cnt_r == 5:
        return 1
    else:
        return 0


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 0
    for i in range(n-5+1):
        for j in range(n-5+1):
            new_arr = arr[i:i + 5]
            for k in range(5):
                new_arr[k] = new_arr[k][j:j+5]   # 5x5로 자름

            result = judge(new_arr)
            if result == 1:
                break
        if result == 1:
            break

    if result == 1:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')
