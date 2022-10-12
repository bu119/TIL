from collections import deque

def bfs():
    cnt = 0
    deq = deque()

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if box[k][i][j] == 1:
                    deq.append((k, i, j))
                elif box[k][i][j] == 0:
                    cnt += 1  # 익지 않은 토마토 수

    if cnt == 0:
        return 0

    while deq:
        k, i, j = deq.popleft()

        for d in range(6):
            nk = k + dk[d]
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and box[nk][ni][nj] == 0:
                deq.append((nk, ni, nj))

                box[nk][ni][nj] = box[k][i][j] + 1
                cnt -= 1

                if cnt == 0:
                    return box[nk][ni][nj] - 1  # 처음 익은 토마토의 시작 값이 1

    return -1


# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 들어있지 않은 칸
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dk = [1, -1, 0, 0, 0, 0]        # 위 아래 왼쪽 오른쪽 앞 뒤
di = [0, 0, 0, 0, 1, -1]
dj = [0, 0, -1, 1, 0, 0]

print(bfs())