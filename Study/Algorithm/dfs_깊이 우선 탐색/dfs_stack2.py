'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 시작점 v

def dfs(v):
    visited = []                    # 방문 처리
    stack = [v]
    while stack:                    # 스택에 남은 것이 없을 때까지 반복
        v = stack.pop()             # 현재 방문하고 있는 정점
        if v not in visited:        # 방문 안한 정점이 있으면
            visited.append(v)       # 방문 처리
            for w in adj_list[v]:
                stack.append(w)
    return visited


V, E = map(int, input().split())    # 정점, 간선
N = V + 1                           # 정점의 개수 만큼 행이 필요
adj_list = [[] for _ in range(N)]
temp = list(map(int, input().split()))

for i in range(E):                  # 인접리스트로 저장하기
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# print(adj_list)  [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
print(dfs(1))   # [1, 3, 7, 6, 5, 2, 4]