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

# 점의 개수 n, 진행된 차례 수 m
n, m = map(int, input().split())
root = list(range(n))

for i in range(m):
    a, b = map(int, input().split())
    # 루트 노드
    x = find(a)
    y = find(b)
    if x == y:
        print(i+1)
        exit(0)

    union(x, y)

print(0)
