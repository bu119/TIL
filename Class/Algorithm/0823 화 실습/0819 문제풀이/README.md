# 스토쿠 검증 (D2)

## 스도쿠에 겹치는 숫자가 없을 경우 1, 그렇지 않을 경우 0 출력하기

- 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
- 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.



1. 행, 열,  3x3행렬에 각 숫자가 하나씩 들어 있는 지 검증한다.



### 수도코드

- 행, 열 검증

```python
for i : (9)
    count = [0] * 10
    for j : (9)
        count[arr[i][j]] += 1
        if count[arr[i][j]] > 1:
            return 0
```

- 사각형 검증

```python
for i : (0,9,3)
    for j :(0,9,3)
        count = [0] * 10    # 초기화
        for x : (3)
            for y : (3)
                count[arr[i+x][j+y]] += 1
                if if count[arr[i][j]] > 1:
                    return 0
```



### Code

```python
def sudoku(arr):
    # 행 검사
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[i][j]] += 1
            if count[arr[i][j]] > 1:
                return 0
    # 열 검사
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[j][i]] += 1
            if count[arr[j][i]] > 1:
                return 0
    # 3x3 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * 10       # 초기화
            for x in range(3):
                for y in range(3):
                    count[arr[i + x][j + y]] += 1
                    if count[arr[i][j]] > 1:
                        return 0
    return 1

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sudoku(arr)}')
```



# 간단한 소인수분해 (D2)

## N = 2^a x 3^b x 5^c x 7^d x 11^e 일때,  a, b, c, d, e 출력하기

### 수도코드

```python
prime = [2, 3, 5, 7, 11]
cnt = [0] * 5
for i : (len(prime))
    while number % prime[i] == 0:
        cnt[i] += 1
        number //= prime[i]
```



### Code

```python
T = int(input())
for tc in range(1, T+1):
    number = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(prime)):
        while number % prime[i] == 0:
            cnt[i] += 1
            number //= prime[i]

    print(f'#{tc} {" ".join(map(str, cnt))}')
```



# 삼성시의 버스 노선 (D3)

## P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하기



### Code

```python
T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 5001
    N = int(input())

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            cnt[j] += 1

    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P):
        temp = int(input())
        print(f'{cnt[temp]}', end=' ')
    print()
```



# 쇠막대기 (D4)

## 잘려진 쇠막대기 조각의 총 개수 구하기

- 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
- 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
- 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
- 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 
- 모든 “()”는 반드시 레이저를 표현한다.
- 쇠대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.



### Code

```python
T = int(input())
for tc in range(1, T+1):
    arr = input()
    cnt = 0
    stack = []
    for i in range(len(arr)):
        if arr[i] == '(':   # 왼쪽괄호
            stack.append(arr[i])
        else:               # 오른쪽 괄호
            stack.pop()
            if arr[i-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
    print(f'#{tc} {cnt}')
```

