from collections import deque
import sys

input = sys.stdin.readline

def bfs(i, j):
    deq = deque()
    deq.append((i, j))

    visited[i][j] = 1
    ssum = population[i][j]
    move = [(i, j)]

    while deq:
        i, j = deq.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and l <= abs(population[i][j] - population[ni][nj]) <= r:
                visited[ni][nj] = 1
                move.append((ni, nj))
                ssum += population[ni][nj]
                deq.append((ni, nj))

    if len(move) > 1:
        for x, y in move:
            population[x][y] = ssum//len(move)

    return len(move)


n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
# l 이상, r 이하

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

day = 0

while True:
    flag = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if bfs(i, j) > 1:
                    flag = 1

    if not flag:
        break
    day += 1

print(day)