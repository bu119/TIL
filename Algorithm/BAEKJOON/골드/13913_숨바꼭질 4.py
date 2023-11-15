from collections import deque

# 경로 찾기
def path(posi, cnt):
    course = []
    for _ in range(cnt + 1):
        course.append(posi)
        posi = visited[posi]
    # 경로가 역순으로 저장되므로 뒤집어준다.
    return reversed(course)

def bfs(v):
    deq = deque()
    deq.append((v, 0))

    while deq:
        # 현재 위치, 몇초 지났는 지
        v, moveCnt = deq.popleft()

        if v == k:
            return moveCnt

        for w in [v - 1, v + 1, v * 2]:
            if 0 <= w <= 100000 and visited[w] == -1:
                deq.append((w, moveCnt+1))
                visited[w] = v


n, k = map(int, input().split())

# 수진이가 더 큰 위치에 있으면 -1로만 동생 위치를 찾을 수 있다.
if n > k:
    print(n-k)
    print(' '.join(map(str, range(n, k-1, -1))))

else:
    # 이전 경로가 저장된다.
    visited = [-1] * 100001
    cnt = bfs(n)
    print(cnt)
    # 경로 출발 순서대로 반환
    route = path(k, cnt)
    print(' '.join(map(str, route)))