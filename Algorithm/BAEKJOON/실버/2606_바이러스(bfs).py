from collections import deque

def bfs(v):
    deq = deque()
    deq.append(v)
    cnt = 0
    visited[v] = 1

    while deq:
        x = deq.popleft()

        for w in link[x]:
            if not visited[w]:
                visited[w] = 1
                cnt += 1
                deq.append(w)
    return cnt


v = int(input())
e = int(input())
link = [[] for _ in range((v+1))]
for i in range(e):
    s, e = map(int, input().split())
    link[s].append(e)
    link[e].append(s)

visited = [0] * (v+1)
ans = bfs(1)
print(ans)