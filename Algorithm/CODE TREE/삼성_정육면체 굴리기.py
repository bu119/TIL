def turn(dir):
    # 주사위 전개도에 번호 매김
    east, west, south, north, top, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 방향에 따라 주사위 면 위치 변화
    if dir == 1: # 동
        dice[0], dice[1], dice[4], dice[5] = top, bottom, west, east
    elif dir == 2: # 서
        dice[0], dice[1], dice[4], dice[5] = bottom, top, east, west
    elif dir == 3: # 북
        dice[2], dice[3], dice[4], dice[5] = bottom, top, south, north
    elif dir == 4: # 남
        dice[2], dice[3], dice[4], dice[5] = top, bottom, north, south

n, m, x, y, k = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(n)]
dk = list(map(int,input().split()))
# 주사위 면
# east, west, south, north, top, bottom
dice = [0]*6
# 1,2,3,4
# 동,서,북,남
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

for d in dk:
    nx = x + di[d]
    ny = y + dj[d]
    if 0 <= nx < n and 0 <= ny < m:
        # 주사위 이동
        turn(d)
        # 칸에 쓰여져 있는 수가 0이면
        if board[nx][ny] == 0:
            # 주사위의 바닥 수가 칸에 복사
            board[nx][ny] = dice[5]
        else:
            # 칸에 쓰여져 있는 수가 0이 아니면
            # 칸에 수가 정육면체 바닥면으로 복사
            dice[5] = board[nx][ny]
            # 해당 칸의 수는 0
            board[nx][ny] = 0
        # 시작 값 변화
        x, y = nx, ny
        print(dice[4])
