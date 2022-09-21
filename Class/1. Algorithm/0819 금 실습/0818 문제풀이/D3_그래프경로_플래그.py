def dfs(v):
    global flag     # 전역 변수
    visited[v] = 1
    if v == G:      # 방문 하자마자 할일
        flag = 1    # 도착하면 더 이상 안내려간다

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)  # 방향성
    S, G = map(int, input().split())
    flag = 0
    dfs(S)
    # print(f'#{tc} {visited[G]}')
    print(f'#{tc} {flag}')