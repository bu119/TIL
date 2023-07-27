# r과 c는 1부터 시작
# 가장 처음에 양분은 모든 칸에 5만큼
# 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익
# 같은 1×1 크기의 칸에 여러 개의 나무 가능

import sys, heapq
input = sys.stdin.readline


# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
def spring():
    global tree, die, live, nutrient

    while tree:
        z, x, y = heapq.heappop(tree)

        if nutrient[x][y] < z:
            die.append((z,x,y))
            continue

        nutrient[x][y] -= z
        live.append((z+1,x,y))


# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
# 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
def summer():
    global die, nutrient

    while die:
        z,x,y, = die.pop()

        nutrient[x][y] += (z//2)


# 가을에는 나무가 번식
# 번식하는 나무는 나이가 5의 배수
# 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
def autumn():
    global tree, live, nutrient

    while live:
        z, x, y = live.pop()

        heapq.heappush(tree, (z,x,y))

        # 번식하는 나무는 나이가 5의 배수
        if z % 5 == 0:
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    heapq.heappush(tree, (1,nx,ny))


# 겨울에는 땅을 돌아다니면서 땅에 양분을 추가
# 각 칸에 추가되는 양분의 양은 A[r][c]
def winter():
    global arr, nutrient

    for i in range(n):
        for j in range(n):
            nutrient[i][j] += arr[i][j]


n, m, k = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

tree = []
for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(tree, (z, x-1, y-1))

nutrient = [[5]*n for _ in range(n)]

year = 0
live = []
die = []
while year != k:

    spring()
    summer()
    autumn()
    winter()

    year += 1

print(len(tree))