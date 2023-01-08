from collections import deque

def bfs(i,j):
    deq = deque()
    deq.append((i,j))
    visited[i][j] = 1
    while deq:
        i, j = deq.popleft()

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:

                if ni == ei and nj == ej:
                    return visited[i][j]

                visited[ni][nj] = visited[i][j] + 1
                deq.append((ni, nj))


t = int(input())
for tc in range(t):
    l = int(input())
    si, sj = map(int,input().split())
    ei, ej = map(int,input().split())

    di = [-2,-1,1,2,2,1,-1,-2]
    dj = [1,2,2,1,-1,-2,-2,-1]
    visited = [[0] * l for _ in range(l)]

    if si == ei and sj == ej:
        print(0)
    else:
        print(bfs(si, sj))