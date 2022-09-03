import sys
sys.stdin = open('testcase/오목_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 0
    for r in range(n-5+1):
        for c in range(n-5+1):
            cnt_dl = 0
            cnt_dr = 0
            for i in range(5):
                cnt_i = 0
                cnt_j = 0
                for j in range(5):
                    # 행 탐색
                    if arr[r+i][c+j] == 'o':
                        cnt_i += 1
                    # 열 탐색
                    if arr[c+j][r+i] == 'o':
                        cnt_j += 1

                if cnt_i == 5 or cnt_j == 5:
                    result = 1
                    break

                # 대각선

                if arr[r+i][c+i] == 'o':
                    cnt_dl += 1

                if arr[r + i][c + 4 - i] == 'o':
                    cnt_dr += 1

            if result == 1:
                break

            # 대각선 오목 탐색
            if cnt_dl == 5 or cnt_dr == 5:
                result = 1
                break

        if result == 1:
            break

    if result == 1:
        print(f'#{tc + 1} YES')
    else:
        print(f'#{tc + 1} NO')

