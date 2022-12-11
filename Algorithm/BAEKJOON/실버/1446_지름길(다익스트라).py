import heapq

def bfs():
    way = []
    heapq.heappush(way, (0, 0))
    dis[0] = 0

    while way:
        shortcut, posi = heapq.heappop(way)

        for e, short in road[posi]:
            ssum = short + shortcut                 # 지름길
            if ssum < dis[e]:                       # 계산한 지름길이 존재하는 거리보다 작으면
                dis[e] = ssum                       # 지름길 값 변경
                heapq.heappush(way, (ssum, e))      # heapq에 추가


n, d = map(int, input().split())
road = [[] for _ in range(d+1)]

# 지름길 없는 원래 거리
for i in range(d):
    road[i].append((i+1, 1))

# 지름길 추가
for _ in range(n):
    s, e, shortcut = map(int, input().split())
    if e <= d:
        road[s].append((e, shortcut))

# 최소 거리를 저장할 곳
dis = [10000] * (d+1)

bfs()

print(dis[d])

