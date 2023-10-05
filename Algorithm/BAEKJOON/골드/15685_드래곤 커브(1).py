# 0세대는 주어진 선
# 1세대는 0세대를 90도 회전후 연결한 2개로 이루어진 선
# 2세대는 1세대를 90도 회전후 연결한 4개로 이루어진 선

# g세대까지 90도 회전한 방향을 저장하는 함수
def move(x, y, d):
    global board

    # 이동 방향 저장
    move_d = [d]

    # g번 시행한다.
    # 1번 시행할 때 마다 움직인 방향을 시계 방향으로 회전하여 추가로 저장한다.
    # 처음 이동 방향에 - 1을 해서 다시 이동하면 된다.
    # -1 하면 시계 방향이 된다. (아니면 이동 방향을 저장)
    for _ in range(g):
        m = len(move_d)
        for k in range(m-1,-1,-1):
            # 방향 저장
            dir = (move_d[k] + 1) % 4
            move_d.append(dir)
            # 위치 저장
            x += dx[dir]
            y += dy[dir]
            if 0 <= x <= 101 and 0 <= y <= 101:
                board[x][y] = 1

    return move_d


# 정사각형인지 판별하는 함수
def find_square(r, c):
    for k in range(3):
        r += dx[k]
        c += dy[k]
        if 0 <= x <= 101 and 0 <= y <= 101 and board[r][c]:
            pass
        else:
            return False
    return True


n = int(input())
board = [[0] * 101 for _ in range(101)]
# 동북서남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
for _ in range(n):
    # x(행), y(열)
    y, x, d, g = map(int, input().split())
    # 방문 체크
    board[x][y] = 1
    # 0세대
    x += dx[d]
    y += dy[d]
    board[x][y] = 1

    # 방향, 위치 미리 탐색 & 저장
    # 연결된 위치, 방향을 저장하는 함수
    # g번 반복 (1세대부터 g세대까지)
    # 회전된 방향을 추가로 저장하기위해 d-1을 하면서 반복 수행
    direction = move(x, y,d)

ans = 0
for i in range(1, 101):
    for j in range(100):
        if board[i][j] and find_square(i, j):
            ans += 1
print(ans)