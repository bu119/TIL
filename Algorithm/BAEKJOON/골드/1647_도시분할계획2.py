import sys
input = sys.stdin.readline

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]

def union(x, y):
    if x > y:
        parents[y] = x
    else:
        parents[x] = y

n, m = map(int, input().split())
info = []
for _ in range(m):
    a, b, c = map(int, input().split())
    info.append((a, b, c))

info.sort(key=lambda x: x[2])
parents = list(range(n + 1))

ans = 0
cnt = n
for a, b, c in info:
    x = find(a)
    y = find(b)

    if x != y:
        union(x, y)
        ans += c
        cnt -= 1

    if cnt == 2:
        break

print(ans)