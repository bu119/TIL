# 상어는 크기와 속도를 가지고 있다.
# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

# 아래는 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다.
# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
# 상어를 잡으면 격자판에서 잡은 상어가 사라진다.

# 상어가 이동한다.
# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다.
# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.

# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다.
# 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
import sys
input = sys.stdin.readline

def move_shark():
    ocean = [[[] for _ in range(c)] for _ in range(r)]
    # 전체 상어 이동
    for row in range(r):
        for col in range(c):
            if sea[row][col]:
                s, d, z = sea[row][col][0]
                x = row
                y = col
                go = 0
                # 상어 속도 만큼 이동
                while go < s:
                    nx = x + di[d]
                    ny = y + dj[d]
                    # 맵 내부에서 이동하는 경우
                    if 0 <= nx < r and 0 <= ny < c:
                        x, y = nx, ny
                        go += 1
                    # 벽과 충돌하는 경우, 방향전환
                    else:
                        d = boundary[d]
                        continue

                # 큰 상어만 남기기
                if not ocean[x][y] or ocean[x][y][0][2] < z:
                    ocean[x][y] = [(s, d, z)]

    return ocean

def catch_shark(j):
    global sea
    # 행 탐색
    for i in range(r):
        if sea[i][j]:
            # 상어를 잡는다.
            s, d, z = sea[i][j].pop()
            return z
    return 0


# 격자판의 크기 R, C와 상어의 수 M
r, c, m = map(int, input().split())
sea = [[[] for _ in range(c)] for _ in range(r)]

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
boundary = {1:2, 2:1, 3:4, 4:3}

for _ in range(m):
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
    rr, cc, s, d, z = map(int, input().split())
    sea[rr-1][cc-1].append((s, d, z))

fishing = 0
for j in range(c):
    # 낚시
    fishing += catch_shark(j)
    # 상어가 이동한다.
    sea = move_shark()
    # shark_eat()
print(fishing)