import sys

def checkState(type, id):
    global now, visited
    if type == "In":
        if id in now:
            # 현재 좌석에 앉아 밥을 먹고 있다
            print(f"{id} already seated.")
            return 1
        else:
            # 이미 밥을 먹고 떠났다
            if id in visited:
                print(f"{id} already ate lunch.")
                return 1
    else:
        if id in visited:
            # 사원이 좌석 (x,y)에 앉아 있었다
            if id in now:
                x,y = now[id]
                arr[x][y] = 0
                del now[id]
                print(f"{id} leaves from the seat ({x+1}, {y+1}).")
                return 1
            else:
                # 이미 밥을 먹고 좌석을 떠났다
                print(f"{id} already left seat.")
                return 1
        else:
            # 아직 점심을 먹지 못했다
            print(f"{id} didn't eat lunch.")
            return 1

    return 0

# 앉을 수 있는 자리인지 판별
def findSeat(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny]:
                # x,y 자리 불가
                return 0
    return 1


# x,y 위치에서 안전도 찾기
def findBigD(x, y):
    global now

    size = n * n + m * m
    for key in now:
        nx, ny = now[key]
        tmp = (x - nx) ** 2 + (y - ny) ** 2
        if tmp < size:
            size = tmp
    return size


n, m, q = map(int, input().split())
arr = [[0] * m for _ in range(n)]
# 현재, 과거거
visited = []
# 우하좌상상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 현재재
now = {}
# 안전도가 가장 높은 좌석을 새로 들어오는 사람에게 배정
for tc in range(q):
    type, id = input().split()

    if checkState(type, id):
        pass
    else:
        if tc == 0:
            arr[0][0] = id
            now[id] = (0, 0)
            print(f"{id} gets the seat (1, 1).")
        else:
            d = 0
            posi = ()
            for i in range(n):
                for j in range(m):
                    # 앉을수있는 좌석이면면
                    if findSeat(i, j):
                        # 이 위치에서 안전도 찾기
                        tmpD = findBigD(i, j)
                        if d < tmpD:
                            d = tmpD
                            posi = (i, j)
            if d and posi:
                # 자리에 앉음
                now[id] = posi
                visited.append(id)
                arr[posi[0]][posi[1]] = id
                print(f"{id} gets the seat ({posi[0]+1}, {posi[1]+1}).")
            else:
                # 가능한 자리 없음
                print("There are no more seats.")