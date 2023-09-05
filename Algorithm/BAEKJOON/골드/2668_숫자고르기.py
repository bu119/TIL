import sys
input = sys.stdin.readline

def bfs(start):
    global ans

    visited = set()
    # 한 개씩만 쌓인다.
    stack = [start]
    visited.add(start)

    while stack:
        v = stack.pop()

        w = graph[v]
        # 방문했으면
        if w in visited:
            # 사이클이 존재하면
            if w == start:
                # 합집합
                ans = ans | visited
            return

        # 방문 안 했으면
        visited.add(w)
        stack.append(w)

    return


n = int(input())
graph = [int(input())-1 for _ in range(n)]

ans = set()
# 사이클이 존재하면 저장
for i in range(n):
    bfs(i)

print(len(ans))
for j in sorted(ans):
    print(j+1)