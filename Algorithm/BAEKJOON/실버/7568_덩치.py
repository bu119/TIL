# 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    w1, h1 = info[i]
    cnt = 1
    for j in range(n):
        w2, h2 = info[j]
        if w1 < w2 and h1 < h2:
            cnt += 1

    print(cnt, end=' ')