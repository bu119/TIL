# 여행 경로가 가능한 것인지 알아보자.
# 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고,
# 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별
import sys
input = sys.stdin.readline

def dfs(v):
    global check, visited
    visited[v] = 1

    if v+1 in set_plan:
        check.add(v+1)

    for w in graph[v]:
        if visited[w] == 0:
            dfs(w)

# 도시의 수
n = int(input())
# 여행 계획에 속한 도시들의 수
m = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            graph[i].append(j)
            graph[j].append(i)

# 같은 도시를 여러 번 방문하는 것도 가능
# 출발지를 시작으로 순서에 관계없이 각 여행지를 방문 가능한지만 체크
plan = list(map(int, input().split()))
set_plan = set(plan)
visited = [0]*n
check = set()
dfs(plan[0]-1)
if set_plan-check:
    print('NO')
else:
    print('YES')