def move(d, p):
    for k in range(len(nut_posi)):
        ni = nut_posi[k][0] + di[d] * p
        nj = nut_posi[k][1] + dj[d] * p
        if ni < 0:
            ni = ni + n
        if nj < 0:
            nj = nj + n
        ni = ni % n
        nj = nj % n
        # 영양제 투입
        tree[ni][nj] += 1
        # 영양제 방문 체크
        nut_visited[ni][nj] = 1
        # 영양제 위치 이동
        nut_posi[k][0] = ni
        nut_posi[k][1] = nj

def grow():
    for x, y in nut_posi:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] >= 1:
                # 나무 성장
                tree[x][y] += 1

def cut():
    global nut_posi
    nut_posi = []
    for x in range(n):
        for y in range(n):
            if nut_visited[x][y] == 0 and tree[x][y] >= 2:
                # 나무 자르기
                tree[x][y] -= 2
                # 영양제 올리기
                nut_posi.append([x,y])


# 격자의 크기 n, 리브로수를 키우는 총 년 수 m
n, m = map(int, input().split())
# 서로 다른 리브로수의 높이
tree = [list(map(int, input().split())) for _ in range(n)]
# 처음 영양제 위치
nut_posi = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

# d는 1번부터 8번까지 각각 → ↗ ↑ ↖ ← ↙ ↓ ↘ 으로 주어집니다.
di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, 1, 1, 0, -1, -1, -1, 0, 1]
# 대각선
dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

for _ in range(m):
    # 이동 방향 d, 이동 칸 수 p
    d, p = map(int, input().split())

    # 영양제 방문 체크
    nut_visited = [[0] * n for _ in range(n)]

    # 영양제 이동
    move(d, p)
    # 영양제 투입 - 나무 성장
    grow()
    # 나무 자르기
    cut()

ans = 0
for i in range(n):
    ans += sum(tree[i])

print(ans)