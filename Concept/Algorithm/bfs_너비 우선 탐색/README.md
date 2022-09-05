비선형구조인 그래프를 탐색하는 방법 (모든 자료를 빠짐없이 검색하는 것이 중요) 

- DFS _ 깊이 우선 탐색
  - 스택 (반복 구조)
  - 재귀
- BFS _ 너비 우선 탐색
  - 큐 (반복 구조)

---

1. A에서 B로 가는 **경로가 있는가?**
   - DFS _ 깊이 우선 탐색
   - BFS _ 너비 우선 탐색
2. A에서 B로 가는 **경로의 개수는?**
   - **DFS** _ 깊이 우선 탐색
3. A에서 B로 가는 **최단 경로의 길이는?**
   - DFS _ 깊이 우선 탐색
   - **BFS** _ 너비 우선 탐색 (주로 사용)

---

# BFS

### 1. 너비 우선 탐색

- 탐색 시작점의 인접한 정점들을 모두 차례로 방문한다.
- 방문했던 정점을 시작으로 다시 인점한 정점을 차례로 방문한다.
- 선입선출



### 2. 경로를 저장하는 방법

- 큐를 사용한다.



### 3. 탐색 순서

<img width="888" alt="BFS 탐색순서" src="https://user-images.githubusercontent.com/109335452/188479419-6343af13-1b53-4ab7-ad2f-34789696c2f4.png">



### 4. 구현 방법

#### 1. 큐

- `Q`가 비면 탐색 종료

<img width="1091" alt="BFS(1)" src="https://user-images.githubusercontent.com/109335452/188479434-3e99ec66-1763-4a76-89a8-5111d035f9e8.png">

<img width="1097" alt="BFS(2)" src="https://user-images.githubusercontent.com/109335452/188479529-913550ff-996c-48b4-8496-87c636f4c562.png">

<img width="1101" alt="BFS(3)" src="https://user-images.githubusercontent.com/109335452/188479699-875c2d93-6741-4626-81ea-7d24729e22dc.png">
<img width="1121" alt="BFS(4)" src="https://user-images.githubusercontent.com/109335452/188479709-b4a1b2f5-81aa-49f1-a6c7-a0404ba9ccbc.png">

<img width="1104" alt="BFS(5)" src="https://user-images.githubusercontent.com/109335452/188479554-430da3d6-9491-4740-85f5-fa2493700997.png">
<img width="1082" alt="BFS(6)" src="https://user-images.githubusercontent.com/109335452/188479562-56e6013b-22c1-4819-8c92-c4c840d14b35.png">



## Code

### 1. 큐

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    q = []                                   # Q 생성
    q.append(v)                              # Q 삽입
    visited[v] = 1                           # 방문체크

    while q:                                 # Q 가 비어있지 않으면
        v = q.pop(0)                         # Q의 첫 번째 원소 반환
        print(v, end=' ')                    # -> 하고픈 일 하기
    for w in adj_list[v]:                    # 인접
            if not visited[w]:               # 방문을 안 했으면
                q.append(w)                  # Q에 넣기
                visited[w] = visited[v] + 1  # 방문체크


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

bfs(1)			# 1
print(visited)  # [0, 1, 2, 2, 0, 0, 0, 0]
```



