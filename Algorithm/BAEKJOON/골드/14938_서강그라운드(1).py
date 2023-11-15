# 양방향 통행이 가능
# 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능
# 예은이가 얻을 수 있는 아이템의 최대 개수?

# 각 지점에서 최소거리를 구한다. (다익스트라)
# 최소거리가 m이하인 지점의 아이템을 더한다.
# 각 점의 아이템을 더한 값을 비교하여 최댓값을 찾는다.
import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    # 최소 거리, 위치
    heap = [(0, start)]
    visited[start] = 0
    # 범위 내 지역 저장
    getItem.add(start)

    while heap:
        dist, curr = heapq.heappop(heap)

        if visited[curr] < dist:
            continue
        # 인접한 지역 탐색
        for next, d in graph[curr]:
            # 다음 지역까지의 이동 거리
            sumDist = dist + d
            # 수색 범위 안에 들어오거나 저장된 거리보다 짧으면
            if sumDist < visited[next]:
                # 최소 거리 갱신
                visited[next] = sumDist
                # 수색 범위 내 지역 추가
                getItem.add(next)
                # 추가 탐색
                heapq.heappush(heap,(sumDist, next))


n, m, r = map(int, input().split())
# 지역 번호와 인덱스 맞추기
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# 아이템 최대 개수 저장
ans = 0
for i in range(1,n+1):
    # 범위 내 지역
    getItem = set()
    # 최소 거리 저장
    visited = [m+1]*(n+1)
    # i 지역에서 다른 지역까지의 최소 거리 찾기
    dijkstra(i)
    # i 지역에서 습득 가능한 아이템 개수 저장
    totalItems = 0
    for j in getItem:
        totalItems += items[j]
    # 아이템 최대 개수 갱신
    ans = max(ans, totalItems)
print(ans)