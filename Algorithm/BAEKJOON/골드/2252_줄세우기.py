from collections import deque
import sys
input = sys.stdin.readline


# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드의 진입 차수 1 빼기
        for j in graph[now]:
            indegree[j] -= 1
            # 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[j] == 0:
                q.append(j)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')


# 노드의 개수와 간선의 개수를 입력 받기
n, m = map(int, input().split())
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(n+1)]
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (n+1)

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    # 정점 A에서 B로 이동 가능
    graph[a].append(b)
    # 진입 차수를 1 증가
    indegree[b] += 1

topology_sort()
