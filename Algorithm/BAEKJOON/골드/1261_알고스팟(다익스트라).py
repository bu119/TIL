import sys, heapq
input = sys.stdin.readline

def dijkstra():
    # 벽 부순 개수, 행 위치, 열 위치
    heap = [(0, 0, 0)]
    # 시작점 0
    visited[0][0] = 0

    while heap:
        cnt, i, j = heapq.heappop(heap)

        # 벽 부순 개수가 저장된 값보다 크면 탐색하지 않는다.
        if visited[i][j] < cnt:
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                # 벽이면 cnt에 1 더 해지고, 빈방이면 그대로 유지된다.
                newCnt = cnt + board[ni][nj]
                # 벽 부순 개수가 저장된 값보다 적으면 갱신한다.
                if newCnt < visited[ni][nj]:
                    visited[ni][nj] = newCnt
                    heapq.heappush(heap, (newCnt, ni, nj))

    return visited[n-1][m-1]


m, n = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[10001]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

print(dijkstra())

