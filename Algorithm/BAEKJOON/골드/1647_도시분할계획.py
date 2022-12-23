import sys
input = sys.stdin.readline

def find(v):
    if root[v] != v:
        root[v] = find(root[v])
    return root[v]

def union(x, y):
    if x < y:
        root[y] = x
    else:
        root[x] = y

# 집의 개수 N, 길의 개수 M
n, m = map(int, input().split())
root = list(range(n+1))
info = []
for _ in range(m):
    a, b, c = map(int, input().split())
    info.append([c,a,b])

info.sort()
ans = 0
cnt = n
for c, a, b in info:
    x = find(a)
    y = find(b)

    if x != y:
        ans += c
        union(x,y)
        cnt -= 1

    if cnt == 2:
        break

print(ans)