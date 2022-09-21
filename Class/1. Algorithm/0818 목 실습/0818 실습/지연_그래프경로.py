def dfs(v):
    # 방문처리
    visited[v] = 1
    result.append(v)
    # v의 인접한 모든 정점(w)에 대해서
    for w in adj_list[v]:
        # 방문 안한 정점이 있으면
        if visited[w] == 0:
            dfs(w)
    return


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    result = []
    for _ in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
    goal = list(map(int, input().split()))
    dfs(goal[0])
    if goal[-1] in result:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')