from itertools import combinations

n, m = map(int,input().split())
place = [list(map(int, input().split())) for _ in range(n)]

house = []
store = []

for i in range(n):
    for j in range(n):
        if place[i][j] == 1:
            house.append((i, j))
        if place[i][j] == 2:
            store.append((i, j))

ans = 999999

for chick in combinations(store, m):    # 순열
    total = 0
    for home in house:                  # 한 집에서 짧은 치킨거리 찾기
        tmp = n*2
        for ch in chick:                # 모든 치킨 집을 탐색하며 짧은 거리 찾기
            tmp = min(tmp, abs(home[0]-ch[0]) + abs(home[1]-ch[1]))
        total += tmp

        if total > ans:
            break

    ans = min(ans, total)               # 도시의 치킨거리끼리 비교
print(ans)