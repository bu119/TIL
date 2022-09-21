import sys
sys.stdin = open('testcase/input_오셀로.txt')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())        # n: 보드 길이(4,6,8), m: 돌 놓는 횟수
    # 흑돌 1, 흰돌 2
    # 3 2 1: (3,2) 흑돌
    board = [[0]*n for _ in range(n)]
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2][n // 2] = 2
    # print(board)
    di = [0, 1, 1, 1, 0, -1, -1, -1]         # 우 부터 시계방향
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    b = 2
    w = 2

    for i in range(m):
        x, y, stone = map(int, input().split())
        x = x-1
        y = y-1
        board[x][y] = stone

        if stone == 1:
            b += 1
        else:
            w += 1

        for j in range(8):
            tmp = []
            for k in range(1, n):
                ni = x + di[j] * k
                nj = y + dj[j] * k
                if stone == 1:
                    if 0 <= ni < n and 0 <= nj < n:
                        if board[ni][nj] == 0:
                            break
                        elif board[ni][nj] == 2:
                            tmp.append((ni, nj))
                        elif board[ni][nj] == 1:
                            if tmp:
                                for r, c in tmp:
                                    board[r][c] = 1
                                    b += 1
                                    w -= 1
                                break
                            else:
                                break

                else:
                    if 0 <= ni < n and 0 <= nj < n:
                        if board[ni][nj] == 0:
                            break
                        elif board[ni][nj] == 1:
                            tmp.append((ni, nj))
                        elif board[ni][nj] == 2:
                            if tmp:
                                for r, c in tmp:
                                    board[r][c] = 2
                                    b -= 1
                                    w += 1
                                break
                            else:
                                break

    print(f'#{tc+1} {b} {w}')



