import sys
from copy import deepcopy


# 각 차고에는 색깔이 있는 자동차가 하나씩 있다.
# 한 턴에 한 칸을 선택하며, 선택한 칸과 상하좌우 칸에 들어있는 자동차의 색이 같다면 모두 사라진다.
# 획득할 수 있는 점수는 사라진 자동차의 개수와 사라지는 차고 칸을 모두 포함하는 가장 작은 직사각형의 넓이의 합
# 자동차들이 사라지고 나면 위에 있는 자동차들이 아래로 떨어져 빈 칸을 채운다.
# 게임을 3차례 반복 했을 때, 주어진 조건에서 얻을 수 있는 가장 큰 점수를 계산

def dfs(idx, ssum, graph):
    global ans

    if idx == 3:
        ans = max(ans, ssum)
        return

    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 방문 안했으면면
            if visited[i][j] == 0:
                print(idx)
                print('bfs전')
                print(graph)
                visited[i][j] = 1
                # 같은 색 갯수, 포함 넓이, 제거 위치
                cnt, area, newGraph, visited = bfs(i, j, graph[i][j], graph, visited)
                # 같은 색 자동차가 존재하면
                if cnt > 1:
                    # 다음 회차 진행
                    print(newGraph)
                    dfs(idx + 1, ssum + cnt + area, newGraph)
                    print('나옴')
                    print(graph)


# 상하좌우 4방향 탐색으로 같은 색 자동차의 개수 구하기
# 사라지는 차고 칸을 모두 포함하는 가장 작은 직사각형의 넓이 구하기 (탐색 가능한 위치의 최대 위치 찾기)
def bfs(x, y, color, currGraph, visited):
    # 같은 색 자동차 위치 저장
    removeCar = []
    newGraph = deepcopy(currGraph)

    # 같은색 개수
    cnt = 1
    # 최소 행렬 값 구하기
    minRow = x
    minCol = y
    # 최대 행렬 값 구하기
    maxRow = x
    maxCol = y
    # 순서관계 없음
    stack = [(x, y)]

    while stack:
        print(currGraph)
        print(visited)
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < n and currGraph[ni][nj] == color and visited[ni][nj] == 0:

                visited[ni][nj] = 1
                stack.append((ni, nj))

                # 같은색 개수
                cnt += 1

                # 최소, 최대 행, 열 값 저장
                minRow = min(minRow, ni)
                minCol = min(minCol, nj)

                # 최대 행, 열 값 저장
                maxRow = max(maxRow, ni)
                maxCol = max(maxCol, nj)

                # 제거해야하는 위치 저장
                removeCar.append((ni, nj))

    if cnt > 1:
        # 2회차, 3회차 시행
        removeCar.append((x, y))
        # 같은 색 자동차 사라지고 그자리 채우기
        removeCar.sort(reverse=True)
        print(newGraph)
        print(removeCar)
        for r, c in removeCar:
            newGraph[r].pop(c)

    area = (maxRow - minRow + 1) * (maxCol - minCol + 1)
    return cnt, area, newGraph, visited


n = int(input())

# 차량 색 저장
garage = [[] for _ in range(n)]
for _ in range(n * 3):
    arr = list(map(int, input().split()))
    for c in range(n):
        garage[c].append(arr[c])

for r in range(n):
    garage[r].reverse()

# 우하좌상상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

ans = 0

# 게임을 3차례 반복
# idx, ssum, graph
dfs(0, 0, garage)
print(ans)