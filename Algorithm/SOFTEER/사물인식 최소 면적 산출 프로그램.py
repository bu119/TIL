def dfs(idx, x1, y1, x2, y2,, color):
    global answer
    # 모든 색을 다 포함했다면 답과 비교해줍니다
    if idx > m:

        X = abs(maxX - minX)
        Y = abs(maxY - minY)
        now = X * Y
        if answer > now:
            answer = now
        return
    # 사실 K개의 색이 모두 있으므로 굳이 if를 표시 안해도 되지만, 꼼꼼하게 할려면 이게 맞을듯합니다.
    if color[num]:
        for nx, ny in color[num]:

            NminX = min(minX, nx)
            NmaxX = max(maxX, nx)
            NminY = min(minY, ny)
            NmaxY = max(maxY, ny)
            tx = NmaxX - NminX
            ty = NmaxY - NminY
            temp = tx * ty
            # 현재까지의 넓이가 answer보다 작으면 dfs를 돌려줍니다
            # 굳이 지금 answer보다 큰 데 굳이 더 돌려주면서 시간초과 나는 것보다는 나으니깐.
            if answer > temp:
                dfs(num + 1, K, NminX, NminY, NmaxX, NmaxY, color)

n, m = map(int,input().split())
color = [[] for _ in range(m + 1)]

for _ in range(n):
    x, y, k = map(int,input().split())
    color[k].append((x, y))

answer = 4000000
# 1번색 좌표 각각마다 dfs시작점으로 잡아줌
for x, y in color[1]:
    dfs (x1, y1, x2, y2, color)

