from collections import deque

def bfs(n):
    visited[n] = 1

    deq = deque()
    deq.append(n)
    while deq:

        v = deq.popleft()
        num = [v + 1, v - 1, v * 2, v - 10]

        for x in num:
            if 0 <= x <= 1000000 and not visited[x]:
                if x == m:
                    return visited[v]
                else:
                    visited[x] = visited[v] + 1
                    deq.append(x)

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    ans = bfs(n)
    print(f'#{tc+1} {ans}')