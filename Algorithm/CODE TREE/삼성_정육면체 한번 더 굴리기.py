def bfs(i, j):
    global score

    # 점수 합
    num = board[i][j]
    score += num
    stack = [(i, j)]
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1

    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and board[ni][nj] == num:
                visited[ni][nj] = 1
                score += num
                stack.append((ni, nj))


def turn(dir):
    # 주사위 전개도에 번호 매김
    east, west, south, north, top, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 방향에 따라 주사위 면 위치 변화
    if dir == 0: # 동
        dice[0], dice[1], dice[4], dice[5] = top, bottom, west, east
    elif dir == 1: # 남
        dice[2], dice[3], dice[4], dice[5] = top, bottom, north, south
    elif dir == 2: # 서
        dice[0], dice[1], dice[4], dice[5] = bottom, top, east, west
    elif dir == 3: # 북
        dice[2], dice[3], dice[4], dice[5] = bottom, top, south, north

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 주사위 면
# east, west, south, north, top, bottom
dice = [3, 4, 2, 5, 1, 6]

# 동, 남, 서, 북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

score = 0

x, y = 0, 0
# 처음 방향 오른쪽
d = 0

for _ in range(m):
    # 이동 좌표
    nx = x + di[d]
    ny = y + dj[d]

    if 0 <= nx < n and 0 <= ny < n:
        pass
    else:
        # 좌표 벗어나면
        d = (d + 2) % 4
        nx = x + di[d]
        ny = y + dj[d]
    # 시작 값 변화
    x, y = nx, ny
    # 인접하며 같은 숫자 찾기
    bfs(x, y)
    # 주사위 면 위치 변경
    turn(d)
    # 방향 변경
    if dice[5] > board[x][y]:
        d = (d + 1) % 4
    elif dice[5] < board[x][y]:
        d = (d - 1) % 4
print(score)
