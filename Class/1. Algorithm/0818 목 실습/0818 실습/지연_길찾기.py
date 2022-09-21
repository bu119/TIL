def dfs(v):
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)
        if visited[check_e] == 1:
            return 1
    return 0

T = 10
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj_list = [[] for _ in range(100)]
    visited = [0] * 100
    temp = list(map(int, input().split()))

    for i in range(E):
        start, end = temp[2 * i], temp[2*i+1]
        adj_list[start].append(end)
    check_s, check_e = 0, 99

    print(f'#{tc} {dfs(check_s)}')