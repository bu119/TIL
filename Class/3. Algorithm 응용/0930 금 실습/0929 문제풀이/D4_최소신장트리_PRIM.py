def prim(s):
    # 출발점 선택
    D[s] = 0
    total = 0
    # 정점의 개수만 큼 반복
    for i in range(V+1):
        # 최소값찾기
        min_v = INF
        for v in range(V+1):
            if visited[v] == 0 and D[v] < min_v:
                min_v = D[v]
                u = v    # 선택한 정점
        # 방문체크, 계산
        visited[u] = 1
        total += adj[PI[u]][u]  # 부모부터 정점까지 거리
        # total += min_v 로 표현해도 된다.

        # 인접한 정점으 가중치 갱신
        # 업데이트 : u에 인접한 정점, 방문 안한 정점 ->  가중치
        for v in range(V+1):
            if adj[u][v] and not visited[v] and D[v] > adj[u][v]:
                D[v] = adj[u][v]
                PI[v] = u
    return total


INF = 987654321                             # 무한대

# 입력
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())            # 정점, 간선
    adj = [[0] * (V+1) for _ in range(V+1)]     # 인접행렬
    D = [INF] * (V+1)                           # 가중치
    visited = [0] * (V+1)                       # 방문체크
    PI = list(range(V+1))                       # 부모 - 내 부모는 나야

    for i in range(E):
        c, p, w = map(int, input().split())     # u는 선택된 정점, v는 이웃한 정점
        adj[c][p] = adj[p][c] = w

    print(f'#{tc} {prim(0)}')
