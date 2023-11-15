import sys, heapq
input = sys.stdin.readline
# 서로 다른 두 도시를 양방향으로 직접 연결
# 1번 도시에서 N번 도시로 자동차를 이용하여 이동
# 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발
# 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용
# 도시마다 주유소의 리터당 가격은 다를 수 있다.

# 1번 도시에서 N번 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.

INF = float('inf')

#  N번 도시까지 가기 위해 드는 최소 비용을 구하는 함수
def dijkstra(maxPrice):
    # 각 정점이 가질 수 있는 최소 비용 마다 총 누적 비용을 체크
    visited = [[INF] * (maxPrice + 1) for _ in range(n + 1)]
    # 전체 비용, 지나온 주유소 최저 가격, 현재 위치
    heap = [(0, price[1], 1)]
    # [현재 도시][지난 온 주유소 리터당 최저 가격] = 현재 까지 최소 비용
    visited[1][price[1]] = 0

    while heap:
        # 전체 비용, 지나온 최저 가격, 현재 위치
        total_cost, min_price, posi = heapq.heappop(heap)

        if posi == n:
            return total_cost

        if visited[posi][min_price] < total_cost:
            continue

        for next_posi, next_dist in graph[posi]:
            new_cost = total_cost + (next_dist * min_price)
            # 다음 도시로 갈 새로운 총 비용이 저장된 비용보다 작다면 갱신
            if new_cost < visited[next_posi][min_price]:
                visited[next_posi][min_price] = new_cost
                # 다음 도시에서 사용할 최소 가격 갱신
                new_price = min(min_price, price[next_posi])
                heapq.heappush(heap, (new_cost, new_price, next_posi))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
price = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

print(dijkstra(max(price)))