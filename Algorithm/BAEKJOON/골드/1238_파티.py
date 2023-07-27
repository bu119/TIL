# 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야
# 도로들은 단방향
# 가장 많은 시간을 소비하는 학생
# 모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있
import heapq
def dijkstra(i):
    visited = [101]*(n+1)
    heap = [(0,i)]
    visited[i] = 0

    while heap:
        ssum, now = heapq.heappop(heap)

        if now == x:
            arrivalX.append((ssum, now))
            return

        for next, next_time in road[now]:
            ssum_time = ssum + next_time
            if ssum_time < visited[]





n, m, x = map(int, input().split())
road = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int, input().split())
    road[s].append((e,t))

arrivalX = []


