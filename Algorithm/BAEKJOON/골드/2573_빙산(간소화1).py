# 빙산의 높이 정보
# 빙산은 일년마다 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오.
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0을 출력한다.
import sys
input = sys.stdin.readline

# 빙산 덩어리 개수 구하기
def bfs(x,y):
    stack = [(x,y)]
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()

        for z in range(4):
            nx = x + di[z]
            ny = y + dj[z]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:

                if sea[nx][ny] > 0:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))
                # 빙산 녹이기
                elif sea[x][y]:
                    sea[x][y] -= 1


n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = 0
iceberg = 0

while True:
    # 빙산 개수 리셋
    iceberg = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if sea[i][j] > 0 and visited[i][j] == 0:
                iceberg += 1
                bfs(i,j)

    if iceberg == 0:
        ans = 0
        break
    elif iceberg >= 2:
        break

    # 1년 적용
    ans += 1

print(ans)