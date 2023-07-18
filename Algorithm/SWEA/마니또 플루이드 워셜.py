def Floyd_Warshall():
    min_cost = 4000001

    # k를 거쳐가는 경우
    for k in range(1, n+1):
        # i에서
        for i in range(1, n+1):
            # j로 갈때
            for j in range(1, n+1):
                if graph[i][k] != 4000001 and graph[k][j] != 4000001:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

                    # 자기 자신으로 돌아오는 비용 체크
                    if i == j:
                        min_cost = min(min_cost, graph[i][j])

    if min_cost == 4000001:
        min_cost = -1

    return min_cost


t = int(input())

for tc in range(t):
    n, m = map(int, input().split())

    graph = [[4000001] * (n+1) for _ in range(n+1)]
    # 자기자신으로 가면 0
    # for node in range(1, n+1):
    #     graph[node][node] = 0

    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x][y] = c

    ans = Floyd_Warshall()
    print(f'#{tc+1} {ans}')