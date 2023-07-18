import sys, heapq
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
def dijkstra():

    heap = [(0,s)]
    dist[s] = 0

    while heap:
        size, cur = heapq.heappop(heap)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist[cur] < size:
            continue

        for nex, nex_size in graph[cur]:

            # 최단거리 경로 이면 (거의 최단 경로 찾을 때 활용)
            if visited[cur][nex]:
                continue

            new_size = size + nex_size
            # 거리가 더 짧은 경우
            if new_size < dist[nex]:
                dist[nex] = new_size
                heapq.heappush(heap, (new_size, nex))

def bfs():
    deq = deque()
    deq.append(d)
    while deq:
        v = deq.popleft()

        # 시작점 도달하면 도착점에서 다시 탐색X
        if v == s:
            # break하면 다른 최단 경로를 확인할 수 없다.
            continue

        for u, p in graph_rev[v]:
            # 도착점에서 출발점으로 갈 때
            # 이전 지점(dist[up_node])에서 up_node까지 거리(rev_size)를 더해서
            # 최단경로에 저장되어 있는 값이 나오면 지난 지점 표시
            if dist[u] + p == dist[v] and not visited[u][v]:
                visited[u][v] = 1
                deq.append(u)


while True:

    n, m = map(int,input().split())

    if n == 0 and m == 0:
        break

    s, d = map(int,input().split())

    graph = [[] for _ in range(n)]
    graph_rev = [[] for _ in range(n)]

    visited = [[0]*n for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int,input().split())
        graph[u].append((v, p))
        graph_rev[v].append((u, p))

    # 최단 거리 저장
    dist = [INF] * n
    dijkstra()

    # 도착점에서 출발점으로 최단 경로 추적 (visited에 방문 표시)
    bfs()

    # 거의 최단 거리 저장
    dist = [INF] * n
    dijkstra()

    if dist[d] == INF:
        print(-1)
    else:
        print(dist[d])

