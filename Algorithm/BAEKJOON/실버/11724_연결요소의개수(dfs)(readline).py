import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = 1

    for w in link[x]:
        if not visited[w]:
            dfs(w)

n, m = map(int, sys.stdin.readline().split())
link = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

cnt = 0
visited = [0] * (n+1)
for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1
        
print(cnt)