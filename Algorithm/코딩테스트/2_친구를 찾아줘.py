from collections import deque

def bfs(target, people, limit):
    visited = [-1]*101
    deq = deque()
    deq.append(target)
    visited[target] = 0

    ori = set()
    new = set()
    while deq:

        node = deq.popleft()

        if visited[node] == 0:
            pass
        elif visited[node] == 1:
            ori.add(node)
        elif visited[node] < limit+1:
            new.add(node)
        else:
            return ori, new

        for p in people[node]:
            if visited[p] == -1:
                visited[p] = visited[node] + 1
                deq.append(p)

    return ori, new

def solution(relationships, target, limit):
    # 1,2 친구이고 2,3이 친구이면 1,3은 친구
    # 원래 알던 친구당 5원 보상
    # 새롭게 알게 된 친구당 10원 보상
    # 새로알게된 친구는 친구로 인정되는 최대 단계를 제한하여 보상 (1이상 100미만)

    people = [[] for _ in range(101)]
    for a, b in relationships:
        people[a].append(b)
        people[b].append(a)

    ori, new = bfs(target, people, limit)
    answer = len(ori) * 5 + len(new) * 10 + len(new)
    return answer


relationships = [[1,2],[2,3],[2,6],[3,4],[4,5]]
# target = 2
# limit = 3

target = 1
limit = 2

print(solution(relationships, target, limit))