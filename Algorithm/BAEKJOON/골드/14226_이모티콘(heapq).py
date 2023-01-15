import sys, heapq
input = sys.stdin.readline

def bfs():
    make = []
    heapq.heappush(make, (0,1,0))
    visited[1][0] = 1
    while make:
        time, emo, clip = heapq.heappop(make)

        if emo == s:
            return time
        # 복사 - 이전 클립보드 내용 덮어쓰기
        if not visited[emo][emo]:
            visited[emo][emo] = 1
            heapq.heappush(make, (time + 1, emo, emo))
        # 붙여넣기
        if 0 < clip and 0 < emo+clip <= s and not visited[emo+clip][clip]:
            visited[emo+clip][clip] = 1
            heapq.heappush(make, (time + 1, emo+clip, clip))
        # 하나 삭제
        if 1 < emo and not visited[emo-1][clip]:
            visited[emo-1][clip] = 1
            heapq.heappush(make, (time + 1, emo-1, clip))


s = int(input())
visited = [[0] * (s+1) for _ in range(s+1)]
print(bfs())