import sys

def dfs(idx, minX, minY, maxX, maxY, area):
    global ans

    # 모든 색을 다 포함하고 최소값보다 작으면 넓이 업데이트
    if idx == m+1:
        if area < ans:
            ans = area
        return

    for xx, yy in color[idx]:
        new_minX = min(minX, xx)
        new_minY = min(minY, yy)
        new_maxX = max(maxX, xx)
        new_maxY = max(maxY, yy)

        size = (new_maxX - new_minX) * (new_maxY - new_minY)

        # 현재 넓이가 최소값 보다 크면 dfs 안함
        if ans > size:
            dfs(idx+1, new_minX, new_minY, new_maxX, new_maxY, size)



n, m = map(int, input().split())

color = [[] for _ in range(m + 1)]

for _ in range(n):
    x, y, k = map(int,input().split())
    color[k].append((x, y))

ans = 4000000

# 1번 색부터 시작
for x, y in color[1]:
    dfs(2, x, y, x, y, 0)

print(ans)