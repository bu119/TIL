# 배열 최소 합 (D3)

 #### [파이썬 SW문제해결 기본 - Stack2]

## 한 줄에서 하나씩 N개의 숫자를 골라 최소 합 출력하기

- 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.



### 풀이 법

- 백트레킹 알고리즘 적용 - DFS 적용하되 유망하지 않으면 부모노드로 돌아감
- 백트레킹 적용하면 불필요한 실행이 대폭 감소
- 현재(부분)합(now_sum)이 min_sum 초과하면 탐색 중지 (가지치기:Pruning)



### Code

```python
def perm(n, k, pr_sum):
    global min_sum            # 최소합을 전역변수로 선언
    if min_sum < pr_sum:
        return

    if n == k:                   # k가 배열의 수와 일치하면 
        if min_sum > pr_sum:     # 현재 합과 (지금까지)최소합 값을 비교
            min_sum = pr_sum     # 현재 합이 더 작으면 대체
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k + 1, pr_sum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]


T = int(input())
for tc in range(1, T + 1):
    min_sum = 987654321    # 큰 수
    N = int(input())   # N X N
    arr = [list(map(int, input().split())) for _ in range(N)]  # 행렬 만듬

    A = list(range(N))
    perm(N, 0, 0)
    print(f'#{tc} {min_sum}')
```





# 노드의 거리 (D3)

#### [파이썬 SW문제해결 기본 - Queue] 

### 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내기

- V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.



### Code

```python
def bfs(v):
    Q = []
    Q.append(v)       # Q에 노드 추가
    visited[v] = 1    # 방문 체크

    while Q:          # 비어 있지 않은 동안 반복
        v = Q.pop(0)  # Q에서 노드를 꺼내서
        #### 하고싶은 일:####
        if v == G:    # 도착지와 일치한다면
            return visited[v] - 1  # 이동거리를 뺀다.
        
		# 노드와 연결된 노트를 탐색
        for w in adj_list[v]:     
            if not visited[w]:    # 방문하지 않은 노드면
                Q.append(w)       # Q에 삽입
                visited[w] = visited[v] + 1  # 이동거리 +1
    return 0  # 경로가 없는 경우 
	# Q가 비면 출발, 도착 노드가 연결되지 않은 것 이므로 0을 리턴

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())  # 노드 개수, 선 개수
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)            # 방문체크 배열
    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    S, G = map(int, input().split()) # 출발 노드, 도착 노드

    print(f'#{tc} {bfs(S)}')
```

