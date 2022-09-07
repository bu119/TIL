'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    q = []                                   # Q 생성
    q.append(v)                              # Q 삽입
    visited[v] = 1                           # 방문체크

    while q:                                 # Q 가 비어있지 않으면
        v = q.pop(0)                         # Q의 첫 번째 원소 반환
        print(v, end=' ')                    # -> 하고픈 일 하기
    for w in adj_list[v]:                    # 인접
            if not visited[w]:               # 방문을 안 했으면
                q.append(w)                  # Q에 넣기
                visited[w] = visited[v] + 1  # 방문체크


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

bfs(1)
print(visited)