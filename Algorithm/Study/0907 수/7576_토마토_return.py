from collections import deque

def bfs(arr):
    q = deque()     # List 시간초과 - deque 사용
    cnt = -1        # 최소 일수
    f_top = 0       # 탐색할 스탭 개수
    s_top = 0       # 뻗어 나온 다음 탐색할 스탭 개수

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:      # 토마토가 있는 자리를 q에 다 넣기
                q.append((i,j))
                f_top += 1
    while q:
        i, j = q.popleft()
        f_top -= 1                  # 앞에 스탭의 좌표를 탐색할 때 마다 개수를 -1
        for z in range(4):          # 4방향 탐색
            ni = i + di[z]
            nj = j + dj[z]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj]==0:
                arr[ni][nj] = 1
                q.append((ni, nj))  # 다음 스탭의 좌표를 q에 넣어줌
                s_top += 1          # 다음 스탭의 개수를 추가
        if f_top == 0:              # 앞의 스탭 좌표를 다 꺼내면 개수를 다음 스탭과 바꿔줌
            f_top, s_top = s_top, f_top
            cnt += 1                # 하루가 지남

    return cnt


m, n = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

di = [0, 1, 0, -1]  # 우하좌상 탐색
dj = [1, 0, -1, 0]

flag = 0

cnt = bfs(arr)

for k in range(n):
    if 0 in arr[k]:
        flag = 1
        break

if flag:
    print(-1)
else:
    print(cnt)