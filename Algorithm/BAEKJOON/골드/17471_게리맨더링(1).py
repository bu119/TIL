from itertools import combinations
import sys
input = sys.stdin.readline

# 1. 구역이 나뉘어 지니?
# 2. 인구 차이가 얼마니?

def bfs(v, group):
    # group으로 방문 체크
    stack = [v]
    total = 0
    while stack:
        v = stack.pop()
        # 인구수 더하기
        total += population[v-1]

        for w in graph[v]:
            # 선거구에 속하면 탐색
            if w in group:
                # 선거구에서 제거 (방문체크)
                group.remove(w)
                stack.append(w)

    # group에 구역이 남아있으면 구역이 모두 연결되어 있지 않음
    if group:
        return 0
    return total


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
# 두 그룹으로 나누기 때문에 N//2+1 이상은 조합이 중복되어 똑같은 작업을 한다.
for k in range(1, n//2+1):
    for g1 in combinations(area, k):
        setG1 = set(g1)
        setG2 = setArea-setG1

        totalG1 = bfs(setG1.pop(), setG1)
        totalG2 = bfs(setG2.pop(), setG2)
        if totalG1 and totalG2:
            # 인구 차이 저장
            diff = totalG1 - totalG2

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