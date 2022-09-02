# Forth (D2)

#### [파이썬 SW문제해결 기본 - Stack2] 

## Forth 코드의 연산 결과를 출력하는 프로그램을 만들기

- Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 
- 숫자는 스택에 넣는다.
- 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
- `.`은 스택에서 숫자를 꺼내 출력한다.
- 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
- 나눗셈의 경우 항상 나누어 떨어진다.
  - `4 / 2 = 2.0` 는 실수형으로 나온다.
  -  `4 // 2 = 2` 를 사용한다.



1. 정수
2. 사칙연산자
3. `.` 



### 수도코드

```python
# 정수
if token.isdigit():        # isdigit(): 숫자니?
    스택 push               # isdigit()를 못쓰면 반대로 사칙연산자와 ., 공백이 아니면 으로 식 세우기
    
# 사칙연산자
if len(stack) >= 2:
    2개 pop → 계산
else:
    return 'error'

# .
if len(stack) == 1:       # . 이 나오면 스택에 값이 하나여야한다.
    return stack.pop()
else:
    return 'error'
```



### Code

```python
def forth(code):
    stack = []
    for token in code:
        # 정수
        if token.isdigit():
            stack.append(token)
        # 사칙연산자
        elif token == '+' or token == '-' or token == '*' or token == '/':
            if len(stack) >= 2:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    stack.append(op1 // op2)     # / 와 // 조심하기
            else:
                return 'error'
        # 점(.)
        elif token == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
 
 
T = int(input())
for tc in range(1, T+1):
    code = list(input().split())
    # print(code)
    print(f'#{tc} {forth(code)}')
```



# 계산기3 (D4)

## 문자열로 이루어진 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램 만들기

1. **중위 표기식  →  후위 표기식**
   - 숫자아닌 것들을 스택에 넣는다.
     - 괄호가 없어진다.
   - 숫자는 문자열에 넣는다.
   - 왼쪽괄호는 연산자 중에서는 밖에 있고 스택에서는 맨 밑에 있는다.
2. **후위 표기식  →  계산**



### 수도코드 (중위 표기식  →  후위 표기식)

```python
for:    
    # 피연산자
    result.append(token)

    # 오른쪽 괄호 ) : 왼쪽 괄호 ( 가 나올때 까지 pop 해서 result에 넣기

    while stack[-1] != '(' :
        result.append(token)
    stack.pop()                 # 왼쪽 괄호 ( 를 만나면 버린다.

    # 왼쪽 괄호 ( , 사칙연산
    if stack:
        while icp[token] <= isp[stack[-1]]:
            result.append(stack.pop())
            if not stack:      # 스택에 아무것도 없으면 빠져나가기 
                break
    stack.append(token)        # if 문 두 개가 여기에 다 걸림
    
while stack:
    result.append(stack.pop())
return '',joun(result)
```



### Code

```python
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}   # 스택 밖에서
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}   # 스택 안에서

def infix_to_postfix(exp):
    stack = []
    result = []
    for token in exp:
        # 피연산자
        if '0' <= token <= '9':
            result.append(token)
        # 오른쪽 괄호
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        # 왼쪽괄호, 사칙연산자
        else:
            if stack:
                while icp[token] <= isp[stack[-1]]:
                    result.append(stack.pop())
                    if not stack: break
            stack.append(token)
    # 스택에 남아있으면
    while stack:
        result.append(stack.pop())
    return ''.join(result)

def calc(exp):
    stack = []
    for token in exp:
        # 피연산자 : push
        if '0' <= token <= '9':
            stack.append(int(token))
        # 연산자: 2개 pop -> 계산 -> push
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(op1 / op2)
    return stack.pop()

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()  # 중위표기식
    postfix = infix_to_postfix(infix) # 후위표기식
    print(f'#{tc} {calc(postfix)}')
```





#  미로 (D3)

#### [파이썬 SW문제해결 기본 - Stack2] 

## NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하기

- 도착할 수 있으면 1, 아니면 0을 출력한다.
- 주어진 미로 밖으로는 나갈 수 없다.

- 100 x 100 은 dfs로 못 푼다.

  - bfs 로 풀기

  - Runtime error
  - 사이즈 잘봐야한다
  - 어떤 오류인지 상세하게 알수없다. (뭔가 초과)

  

1. 상하좌우 순서로 탐색
2. 방문 체크
3. 시작점 V
4. 인접점 W



### 수도코드

```python
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(x, y):
    global flag
    # 가지치기
    if arr[x][y] == 3 :
        flag = 1
        return
    
    # 완전검색
    visited[x][y] = 1  # 방문 체크
    
    for i : (4)
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스, 방문체크, 벽체크
        dfs(nx,ny)
```



### Code

```python
def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j
 
 
def dfs(x, y):
    global flag
    if arr[x][y] == 3:
        flag = 1
        return
 
    # 방문체크
    visited[x][y] = 1         # 방문체크 만들어서 쓰자.
    # 인접한 정점이 방문 안 했으면 dfs
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
 
        # 인덱스, 방문체크, 벽체크
        if nx < 0 or nx == N : continue
        if ny < 0 or ny == N : continue
        if visited[nx][ny] == 1 : continue
        if arr[nx][ny] == 1: continue
        dfs(nx, ny)
 
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    flag = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
 
    sx, sy = find_start(arr)
    dfs(sx, sy)
    print(f'#{tc} {flag}')
```



#  배열 최소 합 (D3)

#### [파이썬 SW문제해결 기본 - Stack2]

## 한 줄에서 하나씩 N개의 숫자를 골라 최소 합을  출력하는 프로그램을 만들기

- NxN 배열에 숫자가 들어있다.
- 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
- 완전 검색은 시간초과
  - 가지치기로 시간을 줄인다.



### Code

```python
def perm(n, k, ssum):
    global ans
    if ans < ssum: return
 
    if n == k:
        if ans > ssum: ans = ssum
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k+1, ssum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]
 
T = int(input())
for tc in range(1, T+1):
    ans = 987654321
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    A = list(range(N))
    perm(N, 0, 0)
    print(f'#{tc} {ans}')
```



# 토너먼트 카드게임 (D3)

#### [파이썬 SW문제해결 기본 - Stack2] 

## N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만들기

- 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는다.
- 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 
- 전체를 두 개의 그룹으로 나누고, 
- 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.



### Code

```python
def win(r1, r2):
    if arr[r1] == arr[r2]:
        return r1
    else:
        if arr[r1] == 1 and arr[r2] == 2:  # 가위 vs 바위
            return r2
        elif arr[r1] == 1 and arr[r2] == 3:  # 가위 vs 보
            return r1
        elif arr[r1] == 2 and arr[r2] == 1:  # 바위 vs 가위
            return r1
        elif arr[r1] == 2 and arr[r2] == 3:  # 바위 vs 보
            return r2
        elif arr[r1] == 3 and arr[r2] == 1:  # 보 vs 가위
            return r2
        elif arr[r1] == 3 and arr[r2] == 2:  # 보 vs 바위
            return r1
 
 
def game(left, right):
    if left == right:
        return left
    else:
        r1 = game(left, (left + right)//2)
        r2 = game((left+right)//2 + 1, right)
        return win(r1, r2)
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(f'#{tc} {game(1, N)}')
```

