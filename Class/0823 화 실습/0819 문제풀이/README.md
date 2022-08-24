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
print(f'#{tc} {''.join(map(str,input()))}')
```



# 삼성시의 버스 노선 (D3)

