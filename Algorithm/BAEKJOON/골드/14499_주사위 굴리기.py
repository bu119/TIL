def move(dir):
    # 주사위 위치 값 저장
    bottom, top, left, right, north, south = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    # 주사위 면 이동
    if dir == 1: # 동
        # bottom, top, left, right 자리
        dice[0], dice[1], dice[2], dice[3] = right, left, bottom, top
    elif dir == 2: # 서
        dice[0], dice[1], dice[2], dice[3] = left, right, top, bottom
    elif dir == 3: # 북
        dice[0], dice[1], dice[4], dice[5] = south, north, bottom, top
    else: # 남
        dice[0], dice[1], dice[4], dice[5] = north, south, top, bottom

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dk = list(map(int, input().split()))
# 주사위 면
# bottom, top, left, right, north, south
dice = [0]*6
# 동서북남
di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]

for d in dk:
    nx = x + di[d]
    ny = y + dj[d]
    if 0 <= nx < n and 0 <= ny < m:
        # 주사위 이동
        move(d)
        # 칸에 쓰여져 있는 수가 0이면
        if board[nx][ny] == 0:
            # 주사위의 바닥 수가 칸에 복사
            board[nx][ny] = dice[0]
        else:
            # 칸에 쓰여져 있는 수가 0이 아니면
            # 칸에 수가 정육면체 바닥면으로 복사
            dice[0] = board[nx][ny]
            # 해당 칸의 수는 0
            board[nx][ny] = 0
        # 시작 좌표 변경
        x, y = nx, ny
        print(dice[1])