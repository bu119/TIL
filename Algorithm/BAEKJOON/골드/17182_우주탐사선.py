def dfs(now, cnt, time):
    global ans

    if cnt == n:
        if ans > time:
            ans = time
        return

    for x in range(n):
        if not visited[x]:
            visited[x] = 1
            dfs(x, cnt + 1, time + arr[now][x])
            visited[x] = 0


n, k = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 플로이드-워셜 : 모든 정점 최단 거리 구하기
for z in range(n):
    for i in range(n):
        for j in range(n):
            # 각 단계마다 특정한 노드 z를 거쳐 가는 경우를 확인
            arr[i][j] = min(arr[i][j], arr[i][z] + arr[z][j])

visited = [0]*n
ans = 1000 * n
visited[k] = 1

# 모든 행성 방문하여 최소 시간 구하기
dfs(k, 1, 0)
print(ans)