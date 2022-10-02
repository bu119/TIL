def prim(s):
    # 시작점 설정
    D[s] = 0
    total = 0
    # 정점의 개수만큼 반복
    for i in range(V+1):
        # 최소값 찾기
        min_value = INF
        # U: 선택된 정점, V: 이웃한 정점
        for v in range(V+1):
            if visited[v] == 0 and min_value > D[v]:
                min_value = D[v]
                u = v
        # 방문체크, 계산
        visited[u] = 1
        total += adj[PI[u]][u]
        # total += min_value 해도 됨 (위 코드 대신)
        # 인접한 정점의 가중치 갱신
        for v in range(V+1):
            if adj[u][v] and not visited[v] and D[v] > adj[u][v]:
                D[v] = adj[u][v]
                PI[v] = u
    return total


INF = 987654321

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]     # 인접행렬
    D = [INF] * (V+1)                           # 가중치
    PI = list(range(V+1))                       # 부모
    visited = [0] * (V+1)                       # 방문체크

    for i in range(E):
        c, p, w = map(int, input().split())
        adj[c][p] = adj[p][c] = w
    print(f'#{tc} {prim(0)}')