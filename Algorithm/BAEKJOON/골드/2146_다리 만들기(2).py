from collections import deque

# 1. 각 섬의 해안가 모두 찾기 (bfs)
def findCoast(i, j):
    # 해안가 위치 저장 (바다와 맞닿은 섬 위치 저장)
    coast = set()
    stack = [(i,j)]
    # 섬 방문 체크 (섬 번호로 방문 체크)
    visited[i][j] = 1

    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                # 바다면, 바다와 맞닿은 섬 위치 저장
                if ocean[ni][nj] == '0':
                    coast.add((i,j))
                else:
                    # 섬이면 방문 체크
                    visited[ni][nj] = 1
                    stack.append((ni,nj))
    return coast

# 2. 해안가에서 다른 섬해안가 까지 최단거리 찾기
def findMindist(a, b):
    global minV
    # a 섬의 해안가 위치
    for r1, c1 in island[a]:
        # b 섬의 해안가 위치
        for r2, c2 in island[b]:
            # 각 섬의 해안가 사이 거리 구하기
            size = abs(r1-r2) + abs(c1-c2) - 1
            # 최단 거리 구하기
            minV = min(minV,size)
            # 최단 거리가 1이면 종료
            if minV == 1:
                print(1)
                exit()


n = int(input())
ocean = [input().split() for _ in range(n)]
visited = [[0]*n for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
minV = 10000
# 섬에 번호를 붙여 구분한다.
island = []
for i in range(n):
    for j in range(n):
        # 방문 안한 섬이면
        if ocean[i][j] == '1' and visited[i][j] == 0:
            # 해당 섬의 해안가 찾기
            coast = findCoast(i, j)
            island.append(list(coast))

m = len(island)
for a in range(m-1):
    for b in range(a+1, m):
        # 섬 2개씩 선택
        findMindist(a,b)

print(minV)