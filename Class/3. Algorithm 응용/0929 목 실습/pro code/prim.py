'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)
'''
'''
10 14
0 1 12
0 2 15
1 3 4
1 4 10
2 5 7
2 6 21
3 4 3
3 7 13
4 5 10
5 8 9
5 9 19
6 9 25
7 8 15
8 9 5
'''
def prim(s):
    # 출발점 선택
    D[s] = 0
    total = 0
    # for 모든 도시가 선택될 때 까지
    for i in range(V):
        # 최소값찾기
        min_v = 987654321
        for v in range(V):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v    # 선택한 도시
        # 방문체크
        visited[u] = 1
        total = adj[[PI[u]]][u]  # 부모부터 정점까지 거리

        # 업데이트 : u에 인접한 정점, 방문 안한 정점 ->  가중치
        for v in range(V):
            if adj[u][v] and not visited[v]:
                if D[v] > adj[u][v]:
                    D[v] = adj[u][v]
                    PI[v] = u

# 입력
V, E = map(int, input().split())    # 정점, 간선
adj = [[0] * V for _ in range(V)]   # 인접행렬
D = [987654321] * V                 # 가중치
visited = [0] * V                   # 방문체크
PI = list(range(V))                 # 부모

for i in range(E):
    s, e, d = map(int, input().split())
    adj[s][e] = adj[e][s] = d

prim(0)
