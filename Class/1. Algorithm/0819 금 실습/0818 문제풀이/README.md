- 삼성전자 코테에는 dp가 안나온다.

- 카카오는 dp가 나온다.

---

# 종이붙이기 (D3)

####  [파이썬 SW문제해결 기본 - Stack1] 

## 20xN 크기의 직사각형에 종이를 붙이는 모든 경우를 찾기

- 10x20, 20x20인 직사각형 종이
- 준비한 종이를 빈틈없이 붙이기
- 재귀, DP 이용가능



### 설계

![](C:\Users\LG\Desktop\PUSH\TIL\Class\0819 금 실습\0818 문제풀이\종이붙이기_dp.png)

### Code (귀납법, 재귀)

```python
def f(k):
    if k <= 1:                     # 기본파트
        return 1
    else:
        return f(k-1) + 2*f(k-2)        # 유도파트
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {f(N//10)}')
```



### Code (DP)

```python
# 메모이제이션
memo = [1, 1]
for i in range(2, 31):
    memo.append(memo[i-1] + 2 * memo[i-2])
 
T = int(input())
for tc in range(1, T+1):
     
    N = int(input())
    print(f'#{tc} {memo[N//10]}')
```



# 반복문자 지우기 (D2)

#### [파이썬 SW문제해결 기본 - Stack1]

## 문자열에서 반복된 문자 지우기

- 지워진 부분은 다시 앞뒤를 연결하는데 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.

- 스택 이용하기



### 설계

```python
for i in range(len(str)):
    if stack:
        stack.append(str[i])
    else:
        if stack[-1] == str[i]:
            stack.pop()
        else:
            stack.append(str[i])
```



### Code

```python
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    stack = []
     
    for i in range(len(str1)):
        # 스택이 비어 있으면
        if len(stack) == 0:
            stack.append(str1[i])
        # 비어 있지 않으면
        else:
            if stack[-1] == str1[i]:
                stack.pop()
            else:
                stack.append(str1[i])
    print(f'#{tc} {len(stack)}')
```



# 괄호검사 (D2)

####  [파이썬 SW문제해결 기본 - Stack1]

## 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하기

### 설계

```python
for i : 0 → len(str1)-1
    if str[i] == '(' or str[i] == '{':
        stack.append(str[i])
    else:
        if len(stack) == 0:
            return 0
        else:
            tmp = stack.pop()
        # 비교
        if str[i] == ')' and tmp != '(':
            return 0
        elif str[i] == '}' and tmp != '{':
            return 0
# 스택이 비어있는지 확인
if stack:
    return 0
return 1
```



### Code

```python
def solve(str1):
    stack = []
    # 문자열 순회
    for i in range(len(str1)):
        # 여는 괄호일 때
        if str1[i] == '(' or str1[i] == '{':
            stack.append(str1[i])
        # 닫는 괄호일 때
        elif str1[i] == ')' or str1[i] == '}':
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop()
            # 같은 쌍인지 검사
            if str1[i] == ')' and tmp != '(':
                return 0
            elif str1[i] == '}' and tmp != '{':
                return 0
    # 스택이 비어있는지 확인
    if stack :
        return 0
    return 1
 
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    print(f'#{tc} {solve(str1)}')
```



# 그래프 경로 (D3)

#### [파이썬 SW문제해결 기본 - Stack1]

## 방향성 그래프에 대해 특정한 두 개의 노드에 경로가 존재하는지 확인하기

- 방향성 그래프 (한 방향)
- DFS 이용하기
- 재귀는 return 조심하기



1. 방문 체크
2. 노드(정점)에 인접한 정점 중  방문 안한 정점이 있으면 순환하기



### 설계

![](C:\Users\LG\Desktop\PUSH\TIL\Class\0819 금 실습\0818 문제풀이\그래프 경로.png)

### Code

```python
def dfs(v):
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)
 
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)   # 방향성
    S, G = map(int, input().split())
    dfs(S)
    print(f'#{tc} {visited[G]}')
```



#### * 도착점에 도착하면 더 이상  밑으로 내려가지 않게 조건을 넣어준다.

#### 1. flag 사용

- 재귀에서 return 자신 없을 때 flag 사용하기
- 되도록 return 쓰지 말고 flag 쓰기

```python
def dfs(v):
    global flag     # 전역 변수
    visited[v] = 1
    if v == G:      # 방문 하자마자 할일
        flag = 1    # 도착하면 더 이상 안내려간다

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)  # 방향성
    S, G = map(int, input().split())
    flag = 0
    dfs(S)
    # print(f'#{tc} {visited[G]}')
    print(f'#{tc} {flag}')
```



#### 2. return 사용 (비추)

- 헷갈린다 (생각을 잘 해야한다.)
- 플래그 안쓰고 return으로 처리하겠다.

```python
def dfs(v):
    # global flag
    visited[v] = 1
    if V == G:       # 방문 하자마자 할일
        # flag = 1
        return 1     # 도착하면 더 이상 안내려간다

    for w in adj_list[v]:
        if visited[w] == 0:
            if dfs(w) == 1:
                return 1
    return 0
	...
```



# 길찾기 (D4)

#### [S/W 문제해결 기본] 4일차 

## 도식화한 지도에서 A도시에서 B도시로 가는 길이 존재하는지 조사하기

### Code

```python
def dfs(v):
    global flag
    visited[v] = 1
    if v == G:
        flag = 1
        # return 1

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)
T = 10
V = 100
S, G = 0, 99
for tc in range(1, T + 1):
    no, E = map(int, input().split())
    temp = list(map(int, input().split()))

    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        a, b = temp[2*i], temp[2*i+1]
        adj_list[a].append(b)  # 방향성

    flag = 0
    dfs(S)

    # print(f'#{tc} {visited[G]}')
    print(f'#{tc} {flag}')
```
