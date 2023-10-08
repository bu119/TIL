# 0 위치 저장
# 0 위치 3개 선택
# bfs로 안전 영역 확인
from itertools import combinations
import sys
input = sys.stdin.readline

# 안전 영역 크기 찾기
def dfs(i, j):
    global safety, virus

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        # 벽 아니고 방문 안했으면 탐색
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj] != 1:
            # 방문 체크
            visited[ni][nj] = 1
            # 안전 영역 개수 세기
            if graph[ni][nj] == 0:
                safety += 1
            else:
                # 바이러스 존재 여부 체크
                virus = True
            dfs(ni, nj)


n, m = map(int, input().split())
graph = []
# 벽 후보가 될 수 있는 빈칸 위치 저장
candidate = dict()
# 후보 key(인덱스) 체크
wallCnt = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for r in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for c in range(m):
        # 빈칸 위치 저장
        if arr[c] == 0:
            candidate[wallCnt] = (r, c)
            wallCnt += 1

# 안전 영역 크기의 최댓값 저장
ans = 0
# 빈칸 3개를 뽑는 경우의 수
for case in combinations(candidate, 3):
    visited = [[0]*m for _ in range(n)]
    # 현재 경우의 안전 영역 저장
    safetyArea = 0
    # 뽑은 3개의 벽 체크
    for idx in case:
        x, y = candidate[idx]
        visited[x][y] = 1

    # 안전 영역 크기 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visited[i][j] == 0:
                # 초기화
                virus = False
                safety = 1
                # 방문 체크
                visited[i][j] = 1
                # 안전 영역 탐색
                dfs(i, j)
                # 안전 영역이면 추가
                if not virus:
                    safetyArea += safety
    # 안전 영역 최댓값 갱신
    ans = max(ans, safetyArea)
print(ans)