# 두 사람이 모두 귀가하는 데 소요되는 예상 최저 택시요금이 얼마인 지
# 지점 번호는 1부터 n까지
# 간선에 표시된 숫자는 두 지점 사이의 예상 택시요금
# 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.

# 지점의 개수 n
# 출발지점을 나타내는 s
# A의 도착지점을 나타내는 a
# B의 도착지점을 나타내는 b
# 지점 사이의 예상 택시요금을 나타내는 fares
import heapq


def bfs(n, s, a, b, info, maxV):
    visited = [0] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, s, 0, 0, 0))
    arrival_charge = {'a': maxV, 'b': maxV, 'ab': maxV}

    while heap:
        cost, now, arrival_a, arrival_b, arrival_ab = heapq.heappop(heap)

        visited[now] = 1

        print(now, a, cost, arrival_a, arrival_b, arrival_ab)

        if now == a:
            arrival_a = 1
            arrival_charge['a'] = min(arrival_charge['a'], cost)

        if now == b:
            arrival_b = 1
            arrival_charge['b'] = min(arrival_charge['b'], cost)

        if arrival_a and arrival_b and not arrival_ab:
            arrival_ab = 1
            arrival_charge['ab'] = min(cost, arrival_charge['ab'])

        print(arrival_a, arrival_b, arrival_ab)
        print(arrival_charge)
        if arrival_a and arrival_b and arrival_ab:
            return arrival_charge

        for e, c in info[now]:
            if not visited[e]:
                heapq.heappush(heap, (cost + c, e, arrival_a, arrival_b, arrival_ab))

    return arrival_charge


def solution(n, s, a, b, fares):
    info = [[] for _ in range(n+1)]
    maxV = 0

    for c, d, f in fares:
        info[c].append((d, f))
        info[d].append((c, f))
        maxV += f

    total = bfs(n, s, a, b, info, maxV)

    if total['a'] + total['b'] < total['ab']:
        answer = total['a'] + total['b']
    else:
        answer = total['ab']
    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))