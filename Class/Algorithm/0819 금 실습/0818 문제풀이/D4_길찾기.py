def dfs(v):
    global flag
    visited[v] = 1
    if v == G:
        flag = 1
        # return 1

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)
T = 10
V = 100
S, G = 0, 99
for tc in range(1, T + 1):
    no, E = map(int, input().split())
    temp = list(map(int, input().split()))

    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        a, b = temp[2*i], temp[2*i+1]
        adj_list[a].append(b)  # 방향성

    flag = 0
    dfs(S)

    # print(f'#{tc} {visited[G]}')    # return을 쓰면
    print(f'#{tc} {flag}')