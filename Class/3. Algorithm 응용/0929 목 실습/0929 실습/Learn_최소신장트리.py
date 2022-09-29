def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([w, v, u])
    edge.sort()
    rep = [i for i in range(V+1)]
    N = V + 1
    cnt = 0
    total = 0
    for w, v, u in edge:
        if find_set(v) != find_set(u):
            cnt += 1
            union(u, v)
            total += w
            if cnt == N-1:
                break
    print(f'#{tc+1} {total}')