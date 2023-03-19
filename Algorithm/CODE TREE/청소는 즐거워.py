
def bfs(i,j):
    order = [(i,j)]
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1
    d = 0

    while i != n//2 or j != n//2 :

        i += di[d]
        j += dj[d]
        if 0 <= i < n and 0 <= j < n and not visited[i][j]:
            visited[i][j] = 1
            order.append((i, j, d))

        else:
            i -= di[d]
            j -= dj[d]
            d = (d+1) % 4
    return order


def move(x, y, d):
    # 우
    if d == 0:
        fly = [(x, y + 1), (x, y + 3), (x - 1, y), (x - 1, y + 1), (x - 1, y + 2), (x - 2, y + 1), (x + 1, y), (x + 1, y + 1), (x + 1, y + 2), (x + 2, y + 1), (x, y + 2)]
    # 하
    elif d == 1:
        fly = [(x + 1, y), (x + 3, y), (x, y - 1), (x + 1, y - 1), (x + 2, y - 1), (x + 1, y - 2), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2), (x + 2, y)]
    # 좌
    elif d == 2:
        fly = [(x, y - 1), (x, y - 3), (x - 1, y), (x - 1, y - 1), (x - 1, y - 2), (x - 2, y - 1), (x + 1, y), (x + 1, y - 1), (x + 1, y - 2), (x + 2, y - 1), (x, y - 2)]
    # 상
    else:
        fly = [(x - 1, y), (x - 3, y), (x, y - 1), (x - 1, y - 1), (x - 2, y - 1), (x - 1, y - 2), (x, y + 1), (x - 1, y + 1), (x - 2, y + 1), (x - 1, y + 2), (x - 2, y)]

    rate = (1, 1, 2, 2, 7, 7, 10, 10, 5)  # 비율




n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

start = n//2

di = [0,1,0,-1]  # 우하좌상
dj = [1,0,-1,0]

order = bfs(0,0)

print(order)