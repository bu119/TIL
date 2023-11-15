# 양방향 통행이 가능
# 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능
# 예은이가 얻을 수 있는 아이템의 최대 개수?
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
# 지역 번호와 인덱스 맞추기
items = [0] + list(map(int, input().split()))
# 수색 범위+1 거리로 초기화
graph = [[m+1] * (n + 1) for _ in range(n + 1)]
# 각 간선에 대한 정보를 입력 받아, 그 값으로 거리 초기화
for _ in range(r):
    # a에서 b로 가는 거리 l
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 자기 자신으로 가는 거리는 0으로 초기화
for i in range(n + 1):
    graph[i][i] = 0

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
# 저장한 최댓값을 출력
for x in range(1, n + 1):
    # x 지역에서 습득 가능한 아이템 개수 저장
    totalItems = 0
    for y in range(1, n + 1):
        if graph[x][y] <= m:
            totalItems += items[y]
    # 최대 아이템 개수 갱신
    ans = max(ans, totalItems)
print(ans)