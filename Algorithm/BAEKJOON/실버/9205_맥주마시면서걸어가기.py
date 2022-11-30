from collections import deque

import sys
input = sys.stdin.readline

def bfs(i,j):

    deq = deque()
    deq.append((i,j))

    while deq:
        i, j = deq.popleft()

        if abs(i-festival[0]) + abs(j-festival[1]) <= 1000:
            return 'happy'

        for k in range(n):
            if visited[k] == 0:
                if abs(i-store[k][0]) + abs(j-store[k][1]) <= 1000:
                    visited[k] = 1
                    deq.append((store[k][0], store[k][1]))
    return 'sad'


t = int(input())
for tc in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))

    visited = [0]*n

    print(bfs(home[0], home[1]))