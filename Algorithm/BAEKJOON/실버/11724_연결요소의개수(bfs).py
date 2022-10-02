from collections import deque

def bfs(x):
    deq = deque()
    deq.append(x)
    visited[x] = 1

    while deq:
        v = deq.popleft()
        for w in link[v]:
            if not visited[w]:
                visited[w] = 1
                deq.append(w)

n, m = map(int, input().split())
link = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

cnt = 0
visited = [0] * (n+1)
for j in range(1, n+1):
    if not visited[j]:
        bfs(j)
        cnt += 1

print(cnt)