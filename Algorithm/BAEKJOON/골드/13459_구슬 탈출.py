# 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다.
# 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 중력을 이용해서 이리 저리 굴려야 한다.
# 상하좌우로 기울이기와 같은 네 가지 동작이 가능하다.

# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.

# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
# 10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
from collections import deque

def leanBalls(x, y, k):
    # 이동 거리 저장
    distance = 0
    # 다음 이동 위치가 벽이 아니고 구멍이 아니면 탐색 종료
    while board[x+di[k]][y+dj[k]] != '#' and board[x][y] != 'O':
        x += di[k]
        y += dj[k]
        distance += 1
    # 위치와 이동거리 반환
    return x, y, distance

def bfs(rx, ry, bx, by):
    deq = deque()
    # 횟수, 빨간 구슬 위치, 파란 구슬 위치
    deq.append((0, rx, ry, bx, by))
    # 방문 체크
    visited = set()
    visited.add((rx, ry, bx, by))

    while deq:
        cnt, rx, ry, bx, by = deq.popleft()

        # 10번 이하로 빨간 구슬을 빼내야한다.
        if cnt > 10:
            return 0

        if board[rx][ry] == "O":
            return 1

        # 기울이기
        for k in range(4):
            # 기울인 방향으로 위치 변화
            nrx, nry, rdist = leanBalls(rx, ry, k)
            nbx, nby, bdist = leanBalls(bx, by, k)

            # 파란 구슬이 구멍에 들어가면 해당 경우는 탐색 안함
            if board[nbx][nby] == "O":
                continue

            # 빨간 구슬, 파란 구슬 위치가 같으면 거리에 따라 늦게 온 구슬 한칸 뒤로 이동
            if nrx == nbx and nry == nby:
                if rdist < bdist:
                    nbx -= di[k]
                    nby -= dj[k]
                else:
                    nrx -= di[k]
                    nry -= dj[k]
            # 구슬 방문 체크
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                deq.append((cnt+1, nrx, nry, nbx, nby))

    return 0


n, m = map(int, input().split())
board = []

for i in range(n):
    row = input()
    board.append(row)
    for j in range(m):
        # 빨간 구슬 위치 찾기
        if row[j] == 'R':
            ri, rj = i, j
        # 파란 구슬 위치 찾기
        if row[j] == 'B':
            bi, bj = i, j

# 우 하 좌 상
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 구슬 탈출 시작
print(bfs(ri, rj, bi, bj))