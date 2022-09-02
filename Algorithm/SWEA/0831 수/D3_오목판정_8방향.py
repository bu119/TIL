import sys
sys.stdin = open('testcase/오목_mine.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 0
    # 8방향 시계 방향으로 탐색
    di = [-1, 0, 1, 1, 1, 0, -1, -1]
    dj = [1, 1, 1, 0, -1, -1, -1, 0]
    for i in range(n):
        for j in range(n):
            cnt_r = 1   # 가로
            cnt_c = 1   # 세로
            cnt_dl = 1  # 왼쪽 대각선
            cnt_dr = 1  # 오른쪽 대각선
            if arr[i][j] == 'o':
                for size in range(1, 3):
                    for k in range(8):
                        ci = i + di[k] * size
                        cj = j + dj[k] * size
                        if 0 <= ci < n and 0 <= cj < n:
                            if arr[ci][cj] == 'o':
                                if k == 0 or k == 4:
                                    cnt_dr += 1
                                elif k == 1 or k == 5:
                                    cnt_r += 1
                                elif k == 2 or k == 6:
                                    cnt_dl += 1
                                elif k == 3 or k == 7:
                                    cnt_c += 1
            if cnt_r == 5 or cnt_c == 5 or cnt_dr == 5 or cnt_dl == 5:
                result = 1
                break
        if result:
            break

    if result:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')