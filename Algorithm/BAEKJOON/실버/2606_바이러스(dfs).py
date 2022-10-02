def dfs(v):
    global cnt
    visited[v] = 1

    for w in link[v]:
        if not visited[w]:
            cnt += 1
            dfs(w)

v = int(input())
e = int(input())
link = [[] for _ in range((v+1))]
for i in range(e):
    s, e = map(int, input().split())
    link[s].append(e)
    link[e].append(s)

visited = [0] * (v+1)
cnt = 0
dfs(1)
print(cnt)