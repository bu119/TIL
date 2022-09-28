from collections import deque

def bfs(v):
    deq = deque()
    deq.append(v)

    visited[v] = 1

    while deq:
        x = deq.popleft()
        for w in num[x]:
            if not visited[w]:
                deq.append(w)
                visited[w] = 1

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    num = [[] for _ in range(n+1)]
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(0, m*2, 2):
        num[arr[i]].append(arr[i + 1])
        num[arr[i+1]].append(arr[i])

    visited = [0] * (n+1)

    for i in range(1, (n+1)):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(f'#{tc+1} {cnt}')