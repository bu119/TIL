from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, k):
    cnt = 0
    deq = deque()
    deq.append((i, j, k))

    while deq:
        i, j, k = deq.popleft()

        if i == n-1 and j == n-1:
            cnt += 1
            continue

        if k == 1:
            connect = [[0, 1, 1], [1, 1, 3]]
        elif k == 2:
            connect = [[1, 0, 2], [1, 1, 3]]
        else:
            connect = [[0, 1, 1], [1, 0, 2], [1, 1, 3]]

        for x,y,z in connect:
            ni = i + x
            nj = j + y
            if 0 <= ni < n and 0 <= nj < n and not house[ni][nj]:
                if z == 3:
                    if house[ni-1][nj] or house[ni][nj-1]:
                        continue
                deq.append((ni, nj, z))
    return cnt


n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

print(bfs(0, 1, 1))