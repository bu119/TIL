# 0 위치 저장
# 0 위치 3개 선택
# bfs로 안전 영역 확인
import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global wall, ans

    # 해당 경우에서 안전 영역 찾기
    if cnt == 3:
        visited = [[0] * m for _ in range(n)]
        # 현재 경우의 안전 영역 저장
        safety = 0
        # 뽑은 3개의 벽 체크
        for x, y in wall:
            visited[x][y] = 1

        # 안전 영역 크기 찾기 (빈칸들 탐색)
        for key in candidate:
            i, j = candidate[key]
            if not visited[i][j]:
                safety += bfs(i, j, visited)
        # 안전 영역 최댓값 갱신
        ans = max(ans, safety)
        return

    # 3개 뽑기
    for posi in range(idx, len(candidate)):
        i, j = candidate[posi]
        graph[i][j] = 1
        wall.append((i,j))
        dfs(posi+1, cnt+1)
        wall.pop()
        graph[i][j] = 0


# 안전 영역 크기 찾기
def bfs(i, j, visited):
    stack = [(i, j)]
    visited[i][j] = 1
    cnt = 1
    virus = False
    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 벽 아니고 방문 안했으면 탐색
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj] != 1:
                visited[ni][nj] = 1
                stack.append((ni, nj))
                # 안전 영역 개수 세기
                if graph[ni][nj] == 0:
                    cnt += 1
                else:
                    # 바이러스 존재 체크
                    virus = True
    # 해당 영역에 바이러스가 존재하면 안전영역 0
    if virus:
        return 0
    return cnt


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
# 빈칸 3개 선택 (벽 후보)
wall = []
# 빈칸 3개를 뽑는 경우의 수
dfs(0, 0)
print(ans)