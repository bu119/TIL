def bfs(v):                                     # k이상 추천, v에서 시작
    cnt = 0                                     # 조건에 맞는 개수 세기
    q = [(v, 0)]                                # (다음 탐색을 시작할 점, 유사도) 초기값이라 유사도 0
    visited = [0] * (N+1)
    visited[v] = 1                              # 시작점에 돌아갈 필요 x (방문체크)
    while q:
        v1, u1 = q.pop()                        # 탐색 시작 점과 이전 점과 유사도
        for v2, u2 in usado[v1]:                # 다음 탐색 점과 이전 탐색 점과의 유사도
            if visited[v2] == 0 and u2 >= k:    # 방문 안했고 유사도가 k 이상이면
                visited[v2] = 1                 # 방문 체크
                cnt += 1                        # 카운트
                q.append((v2, u2))              # 다음 탐색 시작 점
    return cnt

N, Q = map(int, input().split())
usado = [[] for _ in range(N+1)]
for n in range(N-1):
    p, q, r = map(int, input().split())
    usado[p].append((q, r))                     # 그래프 형태로 넣기
    usado[q].append((p, r))

for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(v))