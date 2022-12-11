import heapq
import sys
input = sys.stdin.readline

def bfs(x):
    way = []
    heapq.heappush(way, (0, x))      # 거리, 도착 도시
    dis[x] = 0

    while way:
        distance, city = heapq.heappop(way)

        if distance > k:
            return

        if distance == k:
            cities.append(city)

        for w, e in road[city]:
            cnt = w + distance
            if cnt < dis[e]:
                dis[e] = cnt
                heapq.heappush(way, (cnt, e))

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append((1, b)) # (거리, 도착 도시)

# 최소 거리를 저장할 곳
dis = [1000000] * (n+1)
cities = []
bfs(x)
if cities:
    cities.sort()
    for ans in cities:
        print(ans)
else:
    print(-1)
