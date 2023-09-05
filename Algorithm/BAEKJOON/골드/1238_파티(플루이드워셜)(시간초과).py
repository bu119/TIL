import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[100001]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int, input().split())
    # 단방향 도로
    graph[s][e] = t

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for x in range(1, n + 1):
    graph[x][x] = 0

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
# 각 마을에서 x까지 최단시간 + x에서 각 마을에 도착하는 최단시간 의 최대값 구하기
for i in range(1,n+1):
    ans = max(ans, graph[i][x]+graph[x][i])

print(ans)