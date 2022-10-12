from collections import deque

def bfs(i, j):
    global cnt, size, eat
    global fish

    feed = []
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = cnt

    deq = deque()
    deq.append((i, j))

    while deq and not feed:

        for _ in range(len(deq)):                   # 거리가 같은 위치를 다 탐색하고 먹이가 있는지 판단하기위해
            i, j = deq.popleft()

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and space[ni][nj] <= size and not visited[ni][nj]:
                    deq.append((ni, nj))                    # 갈 수 있는 길 저장
                    visited[ni][nj] = visited[i][j] + 1     # 거리 저장

                    if 0 < space[ni][nj] < size:    # 먹이가 있으면
                        cnt = visited[ni][nj]       # 새로운 탐색을 위해 이 위치까지의 거리 저장
                        feed.append((ni, nj))       # 먹을 수 있는 물고기가 있으면 새로운 탐색을 위해 저장

    return feed                                     # 같은 거리에 있는 먹이 위치를 return

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 1, 0, 0]      # 상 하 좌 우
dj = [0, 0, -1, 1]

fish = [0] * 7          # 각 사이즈의 물고기 개수
size = 2
cnt = eat = 0

for i in range(n):
    for j in range(n):
        if space[i][j] and space[i][j] != 9:
            fish[space[i][j]] += 1
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

# 처음 탐색
restart = bfs(x, y)

# 재 탐색
while sum(fish[1:size]) > 0 and restart:    # 먹을 수 있는 물고기가 전체 공간에 존재하고 새로운 탐색을 위한 물고기 위치가 존재하면
    restart.sort()                          # 먹을수 있는 물고기가 많으면 가장 위, 가장 왼쪽 선택
    x = restart[0][0]
    y = restart[0][1]

    space[x][y] = 0

    eat += 1
    fish[space[x][y]] -= 1              # 물고기 개수 조절

    if size == eat:                     # 상어 사이즈 조절
        size += 1
        eat = 0

    restart = bfs(x, y)

print(cnt)