import sys
input = sys.stdin.readline

def find(v):
    # 루트 노드를 찾을 때 까지 재귀 호출
    if root[v] != v:
        root[v] = find(root[v])
    return root[v]

def union(x, y):
    # 더 작은 루트 노드에 합친다.
    if x < y:
        root[y] = x
    else:
        root[x] = y

V, E = map(int, input().split())
root = list(range(V+1))
tree = []
ans = 0
for i in range(E):
    a, b, c = map(int, input().split())
    tree.append([c, a, b])
tree.sort()

for c, a, b in tree:
    # 루트 노드
    px = find(a)
    py = find(b)
    if px != py:
        union(px, py)
        ans += c

print(ans)
