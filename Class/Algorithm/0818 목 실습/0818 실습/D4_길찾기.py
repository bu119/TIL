import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    # 방문처리
    visited[v] = 1
    # v의 인접한 모든 정점(w)에 대해서
    for w in adj_list[v]:
        # 방문 안한 정점이 있으면
        if visited[w] == 0:
            dfs(w)
        if visited[99] == 1: # 99에 도착 하면 1 반환
            return 1
    return 0 # 99에 도착 안하면 0 반환

for tc in range(10):
    t, v = map(int, input().split())
    adj_list = [[] for _ in range(100)]
    visited = [0] * 100
    temp = list(map(int, input().split()))
    #인접리스트로 저장하기
    for i in range(v):
        s, e = temp[2*i], temp[2*i+1]
        adj_list[s].append(e) # 한 방향

    print(f'#{t+1} {dfs(0)}')