from collections import deque

def bfs(arr):
    global cnt

    q = deque()

    f_top = 0
    s_top = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:      # 토마토가 있는 자리를 q에 다 넣기
                q.append((i,j))
                f_top += 1
    while q:
        i, j = q.popleft()
        f_top -= 1
        for z in range(4):  # 4방향 탐색
            ni = i + di[z]
            nj = j + dj[z]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj]==0:
                arr[ni][nj] = 1
                q.append((ni, nj))
                s_top += 1
        if f_top == 0:
            f_top, s_top = s_top, f_top
            cnt += 1


m, n = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

di = [0, 1, 0, -1]  # 우하좌상 탐색
dj = [1, 0, -1, 0]

cnt = -1
flag = 0

bfs(arr)

for k in range(n):
    if 0 in arr[k]:
        flag = 1
        break

if flag:
    print(-1)
else:
    print(cnt)