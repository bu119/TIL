# 플로이드 워셜 알고리즘

import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 주어진 그래프 정보 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a -> b로 가는 비용은 c
    a, b, c = map(int, input().split())
    # 비용이 다른 같은 a, b가 존재 가능
    graph[a][b] = min(c, graph[a][b])

# k를 거쳐 가는 노드
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # 갈 수 없는 경로인 경우, 0 출력
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()