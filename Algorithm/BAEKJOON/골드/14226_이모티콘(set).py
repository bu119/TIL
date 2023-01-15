from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    deq = deque()
    deq.append((0, 1, 0))
    visited = set()
    visited.add((1,0))
    while deq:
        time, emo, clip = deq.popleft()

        if emo == s:
            return time

        # 복사 - 이전 클립보드 내용 덮어쓰기
        if (emo, emo) not in visited:
            visited.add((emo, emo))
            deq.append((time + 1, emo, emo))
        # 붙여넣기
        if 0 < clip and 0 < emo + clip <= s and (emo + clip, clip) not in visited:
            visited.add((emo + clip, clip))
            deq.append((time + 1, emo + clip, clip))
        # 하나 삭제
        if 1 < emo and (emo - 1, clip) not in visited:
            visited.add((emo - 1, clip))
            deq.append((time + 1, emo - 1, clip))


s = int(input())
visited = [[0] * (s + 1) for _ in range(s + 1)]
print(bfs())