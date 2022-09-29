from collections import deque

def bfs(v):
    deq = deque()
    deq.append(v)

    visited[v] = 1

    while deq:
        x = deq.popleft()
        for w in group[x]:
            if not visited[w]:
                deq.append(w)
                visited[w] = 1

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    group = [[] for _ in range(n+1)]

    for i in range(0, m*2, 2):
        group[num[i]].append(num[i+1])
        group[num[i+1]].append(num[i])

    visited = [0] * (n+1)

    cnt = 0
    for j in range(1, n+1):
        if not visited[j]:
            bfs(j)
            cnt += 1
    print(f'#{tc+1} {cnt}')