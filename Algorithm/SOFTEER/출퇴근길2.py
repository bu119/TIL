import sys
from collections import deque

#### 시간초과

# 종종 길을 바꿔 다니곤 한다.
# 동환이의 출근길과 퇴근길은 가끔 겹친다. 즉, 출근길에 들른 동네를 퇴근길에 다시 지나곤 한다.

# 두 번 들를 수 있는 동네가 그렇게 많지 않음
# 출퇴근길 모두 방문 가능한 동네가 한정된된다.
# 출퇴근길은 단방향 그래프
# 각 동네를 1부터 n까지의 번호가 매겨진 n개의 정점,
# m개의 일방통행의 도로를 단방향 간선으로 삼아 그래프를 만들 수 있다.

# 집 S, 회사 T
# 출퇴근길은 S와 T 사이의 경로

# 출퇴근길에서 목적지 정점을 방문하고 나면 동환이는 더 이상 움직이지 않는다.
# 즉, 출근길 경로에 T는 마지막에 정확히 한 번만 등장
# 퇴근길 경로도 마찬가지로 S는 마지막에 한 번만 등장
# (출근길 경로에 S는 여러 번 등장해도 되고, 퇴근길 경로에 T는 여러 번 등장해도 된다.)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

s, t = map(int, input().split())


def bfs(start, end, destination):
    visited = [0] * (n + 1)
    deq = deque()

    deq.append(start)
    visited[start] = 1

    while deq:
        curr = deq.popleft()

        for p in graph[curr]:

            if p == end:
                return True

            if p == destination:
                continue

            if not visited[p]:
                visited[p] = 1
                deq.append(p)

    return False


ans = 0

for i in range(1, n + 1):
    if i == s or i == t:
        continue

    if bfs(s, i, t) and bfs(i, t, t) and bfs(t, i, s) and bfs(i, s, s):
        ans += 1

print(ans)