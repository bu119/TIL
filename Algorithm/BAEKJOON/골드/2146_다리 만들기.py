from collections import deque
import sys
input = sys.stdin.readline

# 섬을 잇는 다리를 만들겠다
# 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고,
# 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.
# 1. 해안가 찾기 (bfs)
def findCoast(i, j):
    # 해안가 위치 저장 (섬과 맞닿은 바다 위치 저장)
    coast = set()
    stack = [(i,j)]
    # 섬 방문 체크 (섬 번호로 방문 체크)
    visited[i][j] = islandNum

    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                # 바다면, 섬과 맞닿아 있는 바다 위치 저장
                if ocean[ni][nj] == '0':
                    coast.add((ni,nj))
                else:
                    # 섬이면 방문 체크
                    visited[ni][nj] = islandNum
                    stack.append((ni,nj))
    return coast

# 2. 해안가에서 다른 섬 해안가 까지 최단거리 찾기
def bfs(coast):
    # 거리 저장
    dist = [[0]*n for _ in range(n)]
    deq = deque(coast)
    # 해안가 1으로 초기화
    # 섬과 맞닿은 첫번째 바다
    for x, y in deq:
        dist[x][y] = 1

    while deq:
        x, y = deq.popleft()
        # 최소 거리보다 크면 탐색을 종료한다.
        if dist[x][y] >= minV:
            return 10000

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            # 구역안에 들어오고, 방문안했고, 탐색을 시작하는 섬이 아니면 탐색
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0 and visited[nx][ny] != islandNum:
                # 바다면 탐색
                if ocean[nx][ny] == '0':
                    dist[nx][ny] = dist[x][y] + 1
                    deq.append((nx,ny))
                else:
                    # 섬 만나면 거리 반환
                    return dist[x][y]


n = int(input())
ocean = [input().split() for _ in range(n)]
visited = [[0]*n for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
minV = 10000
# 섬에 번호를 붙여 구분한다.
islandNum = 0
for i in range(n):
    for j in range(n):
        # 방문 안한 섬이면
        if ocean[i][j] == '1' and visited[i][j] == 0:
            islandNum += 1
            # 해당 섬의 해안가 찾기
            coast = findCoast(i, j)
            # 최단 거리 찾기
            minV = min(minV, bfs(coast))
print(minV)