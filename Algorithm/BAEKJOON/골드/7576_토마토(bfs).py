from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr):
    global ans, cnt

    deq = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                deq.append((i, j, 0))
            if arr[i][j] == 0:
                cnt += 1

    # 저장될 때부터 모든 토마토가 익어있는 상태
    if cnt == 0:
        return

    while deq:
        i, j, day = deq.popleft()

        if ans < day:
            ans = day

        for k in range(4):  # 4방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                cnt -= 1
                arr[ni][nj] = 1
                deq.append((ni, nj, day+1))

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]  # 우하좌상 탐색
dj = [1, 0, -1, 0]

ans = 0
# 익지 않은 토마토 개수
cnt = 0

bfs(arr)

# 익지 않은 토마토 남아있으면
if cnt:
    ans = -1

print(ans)