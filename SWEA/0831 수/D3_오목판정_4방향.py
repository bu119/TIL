import sys
sys.stdin = open('testcase/오목_mine.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 0
    # 4방향 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선 방향으로 탐색
    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    for size in range(5):
                        ci = i + di[k] * size
                        cj = j + dj[k] * size
                        if 0 <= ci < n and 0 <= cj < n and arr[ci][cj] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        result = 1
                        break
            if result:
                break
        if result:
            break

    if result:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')