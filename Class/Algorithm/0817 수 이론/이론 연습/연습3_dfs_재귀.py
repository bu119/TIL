'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # 방문처리
    visited[v] = 1
    print(v, end=' ')
    # v의 인접한 모든 정점(w)에 대해서
    for w in adj_list[v]:
        # 방문 안한 정점이 있으면
        if visited[w] == 0:
            dfs(w)
    return

V, E = map(int, input().split())  # 정점, 간선
adj_list = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
temp  = list(map(int, input().split()))
#인접리스트로 저장하기
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# print(adj_list)
dfs(1)d