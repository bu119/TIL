# 빙산의 높이 정보
# 빙산은 일년마다 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0을 출력한다.
import sys
input = sys.stdin.readline

# 빙산 덩어리 개수 구하기
def bfs(x,y):
    stack = []
    stack.append((x,y))
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()

        for z in range(4):
            nx = x + di[z]
            ny = y + dj[z]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and sea[nx][ny] > 0:
                visited[nx][ny] = 1
                stack.append((nx,ny))


n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
ice = []
visited = [[0]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = 0
iceberg = 0

# 처음 바다 개수, 빙산 찾기
for i in range(n):
    for j in range(m):
        if sea[i][j]:
            # 주변 바다 개수
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and sea[ni][nj] == 0:
                    cnt += 1

            ice.append((cnt, i, j))
            if visited[i][j] == 0:
                iceberg += 1
                bfs(i,j)

while iceberg < 2 and ice:
    # 빙산 개수 리셋
    iceberg = 0

    # 1년 적용
    ans += 1
    # 존재하는 빙산 인덱스
    idx = []
    # 빙산 녹음 적용
    for zero, r, c in ice:
        sea[r][c] -= zero
        # 방문체크 되돌리기
        visited[r][c] = 0

        # 존재하는 빙산 인덱스 담기
        if sea[r][c] > 0:
            idx.append((r,c))

    ice = []
    for row, col in idx:
        cnt = 0
        for k in range(4):
            nr = row + di[k]
            nc = col + dj[k]
            if 0 <= nr < n and 0 <= nc < m and sea[nr][nc] <= 0:
                cnt += 1

        ice.append((cnt, row, col))
        if visited[row][col] == 0:
            iceberg += 1
            bfs(row, col)

if iceberg < 2:
    ans = 0

print(ans)