import sys
input = sys.stdin.readline

def dfs(v, cnt):
    global flag

    if flag:
        return

    # print(v, end=' ')
    if cnt > 2 and j in cycle[v]:
        flag = 1
        return

    for w in cycle[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w, cnt+1)

# 점의 개수 n : 0 부터 n − 1 까지 고유한 번호가 부여
# 진행된 차례 수 m
n, m = map(int, input().split())
cycle = [[] for _ in range(n)]
ans = 0
start = set()
for i in range(m):
    a, b = map(int, input().split())
    cycle[a].append(b)
    cycle[b].append(a)
    if len(cycle[a]) > 1:
        start.add(a)
    if len(cycle[b]) > 1:
        start.add(b)

    flag = 0
    if i > 2:
        for j in start:
            visited = [0] * n
            visited[j] = 1
            dfs(j, 1)
            # print()
    if flag:
        ans = i+1
        break

print(ans)