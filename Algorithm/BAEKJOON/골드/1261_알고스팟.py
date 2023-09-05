import sys, heapq
input = sys.stdin.readline

def bfs(i, j):
    # 벽 부순 개수, 행 위치, 열 위치
    heap = [(0, i, j)]
    # 방문 체크
    visited[i][j] = 1

    while heap:
        cnt, i, j = heapq.heappop(heap)

        # 종료 조건
        if i == n-1 and j == m-1:
            return cnt

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = 1

                if board[ni][nj] == '0':
                    # 빈 방 이면 cnt 개수를 유지한다.
                    heapq.heappush(heap, (cnt, ni, nj))
                else:
                    # 벽이면 부수고 cnt + 1 을 해준다.
                    heapq.heappush(heap, (cnt+1, ni, nj))


m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

print(bfs(0, 0))