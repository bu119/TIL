import heapq
import sys

def dijkstra(start):
    heap = []
    visited = [4000001]*(n+1)
    visited[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        if visited[now] < cost:
            continue

        for posi, price in graph[now]:
            new_cost = cost + price

            if new_cost < visited[posi]:
                visited[posi] = new_cost
                heapq.heappush(heap, (new_cost, posi))

    return visited


t = int(input())

for tc in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))

    min_cost = 4000001

    for start in range(1, n + 1):
        dist = dijkstra(start)

        for node in range(1, n + 1):
            for next_node, next_cost in graph[node]:
                if next_node == start:
                    min_cost = min(min_cost, dist[node] + next_cost)

    if min_cost == 4000001:
        min_cost = -1

    print(f'#{tc + 1} {min_cost}')
