- 버블정렬, 셀렉트정렬 할 수 있어야한다.



#  색칠하기 (D2) 

#### [파이썬 SW문제해결 기본 - LIST2] 

## 격자에 빨간색과 파란색을 칠해 색이 겹쳐 보라색이 된 칸 수를 구하기

- 주어진 정보에서 같은 색인 영역은 겹치지 않는다.

- flood fill 문제



1. 0으로 세팅
2. 주어진 색의 숫자를 더한다.
3. 3이 되는 칸의 개수 출력



### Code

```python
t = int(input())
size = 10
for tc in range(t):
    n = int(input())
    arr = [[0]*size for _ in range(size)]

    # 색칠하기
    for _ in range(n):  # 할일 없으면 밑줄로 대체간능
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color  # 누적

    # print_arr(arr)
    # print(arr)  값 확인

    # 겹쳐진 칸수 카운트
    cnt = 0
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
```



# 부분집합의 합 (D3)

#### [파이썬 SW문제해결 기본 - LIST2]  

## 집합 A의 부분 집합 중 N개의 원소를 가지고, 합이 K인 부분집합 개수 구하기

- 해당하는 부분집합이 없는 경우 0을 출력
- 모든 부분 집합을 만들어 답을 찾아도 된다. 
- 완전 검색을 해야한다.



### 설계

```python
ans = 0
for i: 1 → (1<<12)
   	sum = cnt = 0
    for j: 0 → 12-1
        if i & (1<<j): # 왼쪽에서 오른쪽으로 넘겨본다
            sum += arr[j]
            cnt += 1
    if cnt == n and sum == k:
            ans += 1
```



### Code

```python
arr = list(range(1, 13))
size = len(arr)
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())

    ans = 0
    for i in range(1, 1 << size):  # 공집합 제외
        sum = cnt = 0
        for j in range(size):
            if i & (1 << j):
                cnt += 1
                sum += arr[j]

        if cnt == n and sum == k:
            ans += 1

    print(f'#{tc + 1} {ans}')
```



# 이진탐색 (D2)

#### [파이썬 SW문제해결 기본 - LIST2]

## 이진 탐색 게임에서 이긴 사람이 누구인지 알아내기

- 책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어진다.

- 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾는다.



1. 정렬이 되어 있어야한다. (sort) (이진탐색)



### Code

```python
def binary_search(arr, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start+end) // 2
        if key == arr[middle]:
            return cnt
        elif key < arr[middle]:
            end = middle
        else:
            start = middle
    # return False
 
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P+1))
 
    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)
 
    ans = '0'
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'
 
    print(f'#{tc} {ans}')
```



# 특별한 정렬 (D3) 

#### [파이썬 SW문제해결 기본 - LIST2]

## 가장 큰 수, 작은 수, 2번째 큰 수,  작은 수 번갈아 정렬하기

- 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력



1. 선택정렬 이용



### Code

```python
def selection_sort(a, n):
    for i in range(10):
        idx = i
        if i % 2 == 0:
            # 최대값
            for j in range(i + 1, n):
                if a[idx] < a[j]:
                    idx = j
        else:
            # 최소값
            for j in range(i + 1, n):
                if a[idx] > a[j]:
                    idx = j
        # 바꾸기
        arr[i], arr[idx] = arr[idx], arr[i]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, n)

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()
```



# Ladder1 (D4)

#### [S/W 문제해결 기본] 2일차

##  주어진 사다리를 타며 도착점에 대응되는 출발점 반환하기

- 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.
- ‘0’ 으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다.



1. 인덱스 체크 먼저 하기
2. 도착점(2)인 밑에서 부터 위로 출발
   - 맨밑의 행에서 2를 찾는다.
3. 네방향 탐색 - 좌 우 상
   - 좌우를 먼저해야 상보다 먼저 시행
   - 상이 먼저면 계속 위로 올라간다.
4. 방문체크



### Code

```python
def find_start(arr):
    for i in range(SIZE):
        if arr[SIZE-1][i] == 2:
            x = SIZE - 1
            y = i
            return x, y

# check 함수 만들어서 찾기

# def check(arr, x, y):
#     if x < 0 or x >= SIZE: return False
#     if y < 0 or y >= SIZE: return False
#     if arr[x][y] == 0: return False
#     if arr[x][y] == 9: return False
#     return True

def ladder(arr, x, y):
    while True:
        if x == 0:
            return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # if check(arr, nx, ny):
            if 0 <= nx < SIZE and 0 <= ny < SIZE and arr[nx][ny] == 1:
                x = nx
                y = ny
                arr[x][y] = 9 # 방문 표시

# 좌우를 먼저 해야함
dx = [0, 0, -1]
dy = [-1, 1, 0]

T = 10
SIZE = 100
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(SIZE)]

    # 시작점 찾기
    x, y = find_start(arr)
    print(f'#{tc} {ladder(arr, x, y)}')
```

