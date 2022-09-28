# 15591. MooTube (Silver)

## USADO가 K 이상인 동영상의 추천 개수 구하기

#### [15591. MooTube (Silver)](https://www.acmicpc.net/problem/15591)

- 두 동영상이 얼마나 가까운 지를 측정하는 단위 “USADO” 
- 다른 동영상으로 가는 경로가 반드시 하나 존재
- 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO 중 최솟값으로 설정
- 주어진 MooTube 동영상에 대해, 값 K를 정해서 그 동영상과 USADO가 K 이상인 모든 동영상 추천

## Idea

- bfs를 활용
- 그래프로 구현


---

## Problem

1. 2차원 배열로 구현하려고 하니 어려움
2. bfs를 그래프로 구현하는 것이 낯설다.


---

## Revision

2. bfs를 그래프로 구현

   ```python
   p, q, r = map(int, input().split())
   usado[p].append((q, r))                     # 그래프 형태로 넣기
   usado[q].append((p, r))
   ```



---

## Code

```python
def bfs(v):                                     # k이상 추천, v에서 시작
    cnt = 0                                     # 조건에 맞는 개수 세기
    q = [(v, 0)]                                # (다음 탐색을 시작할 점, 유사도) 초기값이라 유사도 0
    visited = [0] * (N+1)
    visited[v] = 1                              # 시작점에 돌아갈 필요 x (방문체크)
    while q:
        v1, u1 = q.pop()                        # 탐색 시작 점과 이전 점과 유사도
        for v2, u2 in usado[v1]:                # 다음 탐색 점과 이전 탐색 점과의 유사도
            if visited[v2] == 0 and u2 >= k:    # 방문 안했고 유사도가 k 이상이면
                visited[v2] = 1                 # 방문 체크
                cnt += 1                        # 카운트
                q.append((v2, u2))              # 다음 탐색 시작 점
    return cnt

N, Q = map(int, input().split())
usado = [[] for _ in range(N+1)]
for n in range(N-1):
    p, q, r = map(int, input().split())
    usado[p].append((q, r))                     # 그래프 형태로 넣기
    usado[q].append((p, r))

for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(v))
```

---

## Comment

- bfs 그래프 형태로 구현하기 연습