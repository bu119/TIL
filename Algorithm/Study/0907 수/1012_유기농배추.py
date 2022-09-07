def bfs(i, j):
    global visited
    q = []
    q.append((i, j))         # 배추의 좌표
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)      # 인접하지 않은 배추의 좌표
        for z in range(4):   # 4방향 탐색
            ni = i + di[z]
            nj = j + dj[z]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] and visited[ni][nj] == 0:    # 배추가 있고 방문 안한
                q.append((ni, nj))              # 배추의 좌표를 다음 탐색을 위해 q에 넣어준다.
                visited[ni][nj] = 1             # 방문체크


t = int(input())
for tc in range(t):
    m, n, k = map(int, input().split())  # 배추밭의 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    arr = [[0]*m for _ in range(n)]      # 배추밭 생성
    visited = [[0]*m for _ in range(n)]  # 방문 체크
    cnt = 0

    di = [0, 1, 0, -1]                   # 우하좌상 탐색
    dj = [1, 0, -1, 0]

    for _ in range(k):                   # 배추 생성
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] and visited[i][j] == 0:    # 배추가 있고 방문을 안 했으면
                cnt += 1                            # 카운트
                bfs(i, j)
    print(cnt)