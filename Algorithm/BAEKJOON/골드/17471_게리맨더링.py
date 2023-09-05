from itertools import combinations
import sys
input = sys.stdin.readline

# 1.구역이 나뉘어 지니?
# 2.인구차이가 얼마니?

def bfs(v, group):
    # 방문 체크
    visited = set()
    visited.add(v)

    stack = [v]

    while stack:
        v = stack.pop()

        for w in graph[v]:
            # 선거구에 속하고 방문 안했으면 탐색
            if w in group and w not in visited:
                visited.add(w)
                stack.append(w)
    # 나눈 선거구와 연결되어있는 구역이 같은지 확인
    return visited == group


n = int(input())
population = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]

# 인접한 구역의 정보
for i in range(1,n+1):
    m, *tmp = list(map(int,input().split()))
    for j in range(m):
        graph[i].append(tmp[j])

# 조합으로 구역 나누기
area = range(1, n+1)
setArea = set(area)
minV = 100 * 10 + 1
# 두 그룹으로 나누기 때문에 N//2+1 이상으로 넘어가면 조합이 중복되어 똑같은 작업을 한다.
for k in range(1, n//2+1):
    for g1 in combinations(area, k):
        setG1 = set(g1)
        setG2 = setArea-setG1
        g2 = list(setG2)

        if bfs(g1[0], setG1) and bfs(g2[0], setG2):
            # 인구 차이 저장
            diff = 0

            for p1 in g1:
                diff += population[p1-1]

            for p2 in g2:
                diff -= population[p2-1]

            # 차이가 0이면 최소 경우 이므로 종료!
            if diff == 0:
                print(0)
                exit()

            # 최솟값 찾기
            minV = min(minV, abs(diff))

if minV == 1001:
    print(-1)
else:
    print(minV)