def dfs(i, j):
    global visited
    global cnt_s
    visited[i][j] = 1               # 방문 체크
    cnt_s += 1                      # 각 단지내 집의 수
    for k in range(4):              # 4방향 탐색
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] and visited[ni][nj] == 0:
            dfs(ni, nj)             # 다시 탐색
    return cnt_s


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

di = [0, 1, 0, -1]                  # 우하좌상
dj = [1, 0, -1, 0]

cnt_b = 0                           # 총 단지수
cnt = []

for i in range(n):
    for j in range(n):
        if arr[i][j] and visited[i][j] == 0:
            cnt_b += 1              # 총 단지수
            cnt_s = 0               # 각 단지내 집의 수 초기화
            cnt.append(dfs(i,j))    # 각 단지내 집의 수 추가

print(cnt_b)
cnt.sort()
for z in cnt:
    print(z)