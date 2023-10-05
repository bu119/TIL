import sys
input = sys.stdin.readline

# 방향성이 없는 그래프
n, e = map(int, input().split())
# 최댓값
INF = 200000001
dist = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c

v1, v2 = map(int, input().split())

# 플루이드 워셜
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

# 1, v1, v2, n
case1 = dist[1][v1] + dist[v1][v2] + dist[v2][n]
# 1, v2, v1, n
case2 = dist[1][v2] + dist[v2][v1] + dist[v1][n]

ans = min(case1, case2)
if ans < INF:
    print(ans)
else:
    print(-1)