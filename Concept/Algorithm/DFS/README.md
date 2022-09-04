비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함. 

- 깊이 우선 탐색 (DFS)
- 너비 우선 탐색 (BFS)

---

# DFS

### 1. 깊이 우선 탐색

- 출발점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면,
- 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여
- 모든 정점을 방문하는 순회방법



### 2. 경로를 저장하는 방법

1. **스택**
   - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용한다.
2. **재귀**
   - 일반적으로 코드가 깔끔하기 때문에 선호하는 방법이다. 
   - 노드(정점)에 방문하면 그 노드(정점)를 출력하고 그것의 자식들을 재귀 호출한다.



### 3. 구현 방법

#### 1. 스택

1. 탐색 시작 노드(`v`)를 스택에 삽입(`push`) 하고 방문 처리 한다.
2. 스택의 최상단 노드(`v`)에 인접한 노드 중에
   - 방문하지 않은 인접 노드(`w`)가 있으면 인접 노드(`w`)를 스택에 넣고(`push`) 방문 처리 한다. (2번 반복)
   - 방문하지 않은 인접 노드(`w`)가 없으면 탐색의 방향을 바꾸기 위해 스택의 최상단 노드(`v`) 를 꺼낸다. (`pop`) (2번 반복)
3. 스택이 공백이 될 때까지 2번을 반복한다.



#### 2. 재귀

1. 노드에 방문하면 그 노드를 출력하고 그것의 자식들을 재귀 호출한다.
2. 노드의 자식의 자식의 자식... 을 계속 호출하고 들어간 다음
3. 더이상 자식이 없으면 하나 올라와서 올라온 지점의 다른 경로로부터 탐색을 다시 시작한다.



## Code

### 1. 스택

1.  초기상태
   - 배열 visited를 False로 초기화
   -  공백의 스택 생성
2. 출발 정점 A를 시작으로 깊이 우선 탐색 시작
3. 정점 A에 방문하지 않은 인접 정점이 있으면 A를 스택에 push하고, 인접 정점을 오름차순에 따라 선택하여 계속 탐색한다.
   - A - B - D - F - E - C

![DFS(1)](C:\Users\LG\Desktop\PUSH\TIL\Concept\Algorithm\IMG\DFS(1).png)

4. 정점 C에서 방문하지 않은 인접 정점이 없으므로, 

   마지막 정점으로 돌아가기위해 스택을 pop하여 받은 정점 E에 방문하지 않은 인접 정접이 있는지 확인한다.

![DFS(2)](C:\Users\LG\Desktop\PUSH\TIL\Concept\Algorithm\IMG\DFS(2).png)

5. pop한 정점에 방문하지 않은 인접 정점이 나올때까지 pop을 반복한다.
6. 정점 F에 방문하지 않은 정점 G가 있으므로 F를 스택에 push 하고, 인접 정점 G를 선택하여 탐색을 계속한다.

![DFS(3)](C:\Users\LG\Desktop\PUSH\TIL\Concept\Algorithm\IMG\DFS(3).png)

7. 정점 G에서 방문하지 않은 인접 정점이 없으므로, 

   마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 F에 대해서 방문하지 않은 정점이 있는지 확인한다.

8. 반복 수행하여 A까지 되돌아 가게 되고 스택이 비어 중단된다.

   - G - F - D - B - A

   ![DFS(4)](C:\Users\LG\Desktop\PUSH\TIL\Concept\Algorithm\IMG\DFS(4).png)

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 시작점 v

def dfs(v, N):
    top = -1                
    
    visited[v] = 1                  # 시작점 방문 표시
    print(v, end=' ')               # 방문해서 할 일: 방문한 곳 출력
    
    while True:
        for w in adj_list[v]:       # v의 인접 정점 중 
            if visited[w] == 0:     # 방문 안한 정점 w가 있으면
                top += 1            # push(v)
                stack[top] = v
                v = w               # v <- w (w에 방문)
            
                visited[w] = 1      # visited[w] <- true
                print(v, end=' ')   # 방문해서 할 일: 방문한 곳 출력
                break
        else:                       # w가 없으면 (for문을 나온 상황)
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top = -1
            else:                   # 스택이 비어있으면
                break               # while 빠져나옴


V, E = map(int, input().split())    # 정점, 간선
N = V + 1                           # 정점의 개수 만큼 행이 필요
adj_list = [[] for _ in range(N)]
temp  = list(map(int, input().split()))

for i in range(E):                  # 인접리스트로 저장하기
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

visited = [0] * N                   # visited 생성 (초기화)
stack = [0] * N                     # stack 생성 (초기화)
dfs(1, N)
print()

# 1 2 4 6 5 7 3 
```



- 방문순서 다르다.

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 시작점 v

def dfs(v):
    visited = []                    # 방문 처리
    stack = [v]
    while stack:                    # 스택에 남은 것이 없을 때까지 반복
        v = stack.pop()             # 현재 방문하고 있는 정점
        if v not in visited:        # 방문 안한 정점이 있으면
            visited.append(v)       # 방문 처리
            for w in adj_list[v]:   # 이 과정 때문에 스택에 들어가는 순서가 달라서 방문 순서가 다르게됨
                stack.append(w)
    return visited


V, E = map(int, input().split())    # 정점, 간선
N = V + 1                           # 정점의 개수 만큼 행이 필요
adj_list = [[] for _ in range(N)]
temp = list(map(int, input().split()))

for i in range(E):                  # 인접리스트로 저장하기
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)
    
# print(adj_list)   [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
print(dfs(1))       # [1, 3, 7, 6, 5, 2, 4]
```





### 2. 재귀

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):

    visited[v] = 1                # 방문처리
    print(v, end=' ')

    for w in adj_list[v]:         # v의 인접한 모든 정점(w)에 대해서
        if visited[w] == 0:       # 방문 안한 정점이 있으면
            dfs(w)
    return

V, E = map(int, input().split())  # 정점, 간선
adj_list = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
temp  = list(map(int, input().split()))

for i in range(E):                # 인접리스트로 저장하기
    s, e = temp[2*i], temp[2*i+1]
    adj_list[s].append(e)
    adj_list[e].append(s)

# print(adj_list)     [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
dfs(1)                # 1 2 4 6 5 7 3 
```



