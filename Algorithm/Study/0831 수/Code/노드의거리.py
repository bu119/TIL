import sys; sys.stdin = open('노드의거리_input.txt')

def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        #### 하고싶은 일:####
        if v == G:
            return visited[v] - 1

        for w in adj_list[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0  # 경로가 없는 경우

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S)}')
