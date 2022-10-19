from collections import deque

def bfs(i, j, wall):               # k는 벽 부수기 여부 (1:부숨)
    deq = deque()
    deq.append((i, j, wall))
    visited[i][j][wall] = 1        # 방문 체크

    while deq:
        i, j, wall = deq.popleft()

        if i == n-1 and j == m-1:
            return visited[i][j][wall]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][wall] == 0:      # 방문 안 했으면
                if mapp[ni][nj] == 0:                                           # 벽 없으면
                    visited[ni][nj][wall] = visited[i][j][wall] + 1             # 방문 체크
                    deq.append((ni, nj, wall))

                if mapp[ni][nj] == 1 and wall == 0:                          # 벽이 있고 안 부쉈으면
                    visited[ni][nj][1] = visited[i][j][wall] + 1             # 벽 부순 상태 방문 체크
                    deq.append((ni, nj, 1))

    return -1


n, m = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(n)]

di = [0, 1, 0, -1]  # 우하좌상 탐색
dj = [1, 0, -1, 0]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, 0))
# print(visited)