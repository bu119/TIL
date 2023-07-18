# N명의 학생들은 총 M개의 마니또 관계를 맺는다.
# 한 학생이 한 학생에게 C 비용 만큼의 선물을 일방적으로 주는 것을 뜻한다.
# 그 반대는 해당하지 않는다.
# 예를 들어 X와 Y가 X → Y 마니또 관계를 맺으면, 그 반대인 X ← Y는 수행하지 않는다.
# 총 선물 비용이 가장 작은 마니또 사이클을 찾는 프로그램
# 두 학생이 주고받는 마니또 관계도 마니또 사이클에 포함됨에 주의하시오.
# 선물 비용이 가장 작은 마니또 사이클의 비용을 출력한다.
import heapq
def dijkstra():
    heap = []
    for k in range(1,n+1):
        if graph[k]:
            # 총 비용, 위치
            heapq.heappush(heap, (0, k, k))
            # print((0, k, k))

    while heap:
        cost, now, start = heapq.heappop(heap)
        # print(cost, now, start)

        if now == start and cost > 0:
            return cost

        for posi, price in graph[now]:
            # print(posi,price)
            new_cost = cost + price
            heapq.heappush(heap, (new_cost, posi, start))

    return -1



t = int(input())
for tc in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x].append((y,c))

    ans = dijkstra()

    print(f'#{tc+1} {ans}')



