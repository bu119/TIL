import sys
sys.stdin = open("gr_input.txt", "r")

def dfs(start, end):
    # 방문처리
    visited[start] = 1
    # v의 인접한 모든 정점(w)에 대해서
    for w in adj_list[start]:
        # 방문 안한 정점이 있으면
        if visited[w] == 0:
            dfs(w, end)
        if visited[end] == 1: # end에 도착 하면 1 반환
            return 1
    return 0 # end에 도착 안하면 0 반환

t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for n in range(E):
        s, e = list(map(int, input().split()))
        adj_list[s].append(e)

    start, end = map(int, input().split())
    print(f'#{tc+1} {dfs(start, end)}')