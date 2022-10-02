def dijkstra(s):
    # 출발점 설정
    D[s] = 0
    # 0 ~ N 번 반복
    for _ in range(N + 1):
        # 최소값 찾기
        min_value = INF
        for v in range(N + 1):
            if not visited[v] and D[v] < min_value:
                min_value = D[v]
                u = v
        # 방문처리
        visited[u] = 1
        # if u == N:
        #     return D[u]

        # 방문안한 인접 정점 갱신
        for v in range(N + 1):
            if adj[u][v] and not visited[v]:
                if D[v] > D[u] + adj[u][v]:
                    D[v] = D[u] + adj[u][v]


INF = 987654321
T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]  # 인접행렬
    D = [INF] * (N + 1)  # 가중치
    visited = [0] * (N + 1)

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # 방향성 있음

    dijkstra(0)
    print(f'#{tc} {D[N]}')