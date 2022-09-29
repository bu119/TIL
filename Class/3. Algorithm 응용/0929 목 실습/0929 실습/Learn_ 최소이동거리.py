def dijkstra(s, V):
    U = [0]*(V+1)       # 비용이 결정된 정점을 표시
    U[s] = 1            # 출발점 비용 결정
    for i in range(V+1):
        D[i] = adjM[s][i]

    # 남은 정점
    for _ in range(V):
        minV = 10000
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1                # 비용 결정
        for v in range(V+1):
            if 0 < adjM[w][v] < 10000:
                D[v] = min(D[v], D[w]+adjM[w][v])

t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    adjM = [[10000]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        adjM[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0]*(V+1)
    dijkstra(0, V)
    print(f'#{tc+1} {D[-1]}')
