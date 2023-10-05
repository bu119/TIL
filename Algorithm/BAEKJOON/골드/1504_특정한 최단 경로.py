import sys, heapq
input = sys.stdin.readline

# start에서 각 점까지의 최단거리
def dijkstra(start):
    visited = [INF]*(n+1)
    heap = []
    # 최단거리, 시작 위치 저장
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    while heap:
        # start부터 현재 위치까지 최단거리, 현재 위치
        dist, v,  = heapq.heappop(heap)

        # 현재 위치까지 거리보다 저장된 거리가 짧으면 해당 경우는 탐색 안함
        if visited[v] < dist:
            continue
        # 다음 위치, 다음 위치까지 거리
        for w, nextDist in graph[v]:
            totalDist = dist + nextDist
            # 새로 구한 거리가 저장된 거리보다 짧으면 갱신
            if totalDist < visited[w]:
                visited[w] = totalDist
                heapq.heappush(heap, (totalDist, w))
    # start부터 저장된 최단거리
    return visited


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    # 방향성이 없는 그래프
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 최댓값
INF = 200000001

# 출발점이 다른 3가지 경우 (1, v1, v2)
start1 = dijkstra(1)
startV1 = dijkstra(v1)
startV2 = dijkstra(v2)
# 1, v1, v2, n
case1 = start1[v1] + startV1[v2] + startV2[n]
# 1, v2, v1, n
case2 = start1[v2] + startV2[v1] + startV1[n]
# 최단 경로
ans = min(case1, case2)
if ans < INF:
    print(ans)
else:
    print(-1)