# 정육면체 주사위를 사용
# 10×10, 총 100개의 칸으로 나누어져 있는 보드판
# 플레이어는 주사위를 굴려 나온 수만큼 이동
# 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동
# 도착한 칸이 사다리면, 사다리를 타고 위로 올라간다.
# 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.
# 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고,
# 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

from collections import deque
import sys
input = sys.stdin.readline

# 구현
def bfs(start):
    visited = [0]*101
    deq = deque()
    # 플레이어 위치, 주사위 횟수
    deq.append((start, 0))
    visited[start] = 1
    while deq:
        curr, cnt = deq.popleft()

        # 100번 칸에 도착
        if curr == 100:
            return cnt
        # 주사위 굴리기
        for k in range(1, 7):
            next = curr + k
            if next <= 100 and not visited[next]:
                visited[next] = 1
                # 사다리 or 뱀을 만나서 이동할 경우
                if board[next]:
                    # 이동 위치
                    next = board[next]
                    # 방문한 위치면 탐색 안함
                    if visited[next]:
                        continue
                    # 방문하지 않은 위치면 방문 체크
                    visited[next] = 1

                deq.append((next, cnt + 1))


# 사다리의 수 N, 뱀의 수 M
n, m = map(int, input().split())
board = [0]*101

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

print(bfs(1))