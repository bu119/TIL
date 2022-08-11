# < 0809 문제 풀이 >

- 알고리즘은 인덱스 조절 연습하기
- 설계(수도코드)는 중요한 부분만 위주로 하기



# min max (D2)

- 문제 :  [min max](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYIZDyM6218DFAV6&contestProbId=AXiv8PR6QT8DFAW9&probBoxId=AYJ_4ThKGR8DFAVG&type=USER&problemBoxTitle=08-09&problemBoxCnt=5)

- 최대값의 인덱스



## 설계

```python
min_value = 0
max_value = 1000000
if i : 0 → n-1
    if min_value > arr[i]:
        min_value = arr[i]
    if max_value < arr[i]:
        max_value = arr[i]

ans = max_value - min_value
```



## 구현 (min_max.py)

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    min_value = 1000000
    max_value = 0
 
    for i in range(N):
        if min_value > arr[i]:
            min_value = arr[i]
        if max_value < arr[i]:
            max_value = arr[i]
 
    print(f'#{tc} {max_value - min_value}')
```



# 숫자 카드  (D2)

- 문제 :  [숫자카드](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYIZDyM6218DFAV6&contestProbId=AXjJn4oKSqoDFAW9&probBoxId=AYJ_4ThKGR8DFAVG&type=USER&problemBoxTitle=08-09&problemBoxCnt=5)

- 카운팅 이용해서 풀기!!!

  

## 설계

```python
for i : 0 → n-1
    count[num[i]] += 1
    num // = 10    
```



| 인덱스 | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 개수   |      |      |      |      |      |      |      |      |      |      |



## 구현 (구간합.py)

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = int(input())
    
    '''
    cut = 0

    길이를 모를 때는 while문을 돌리면서 count += 1 을 하면 구할 수 있음
    while num > 0:
    num //= 10
    '''

    # 카운팅
    count = [0] * 10
    for i in range(N):
        count[num % 10] += 1
        num //= 10

    # 최대값의 인덱스
    max_idx = 0
    for i in range(1, 10):
        if count[max_idx] <= count[i]:
            max_idx = i

    print(f'#{tc} {max_idx} {count[max_idx]}')
```



# 구간합 (D2)

- 문제 :  [구간합](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXf2zXgqZDcDFAUO&solveclubId=AYIZDyM6218DFAV6&problemBoxTitle=08-09&problemBoxCnt=5&probBoxId=AYJ_4ThKGR8DFAVG)

- 2차원 배열의 구간합 풀어보기 ( 문제 : [2001. 파리 퇴치](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq))



## 설계

```python
# 1. 전체 초기화 (여기!!)
max_value = min_value = 0 

for i : 0 → n-m
    
#   2.sum은 할 때 마다 초기화 (여기!!)
    total = 0
    
    for j : 0 → m-1
        
#       3. 초기화 위치는 어디?
        
        total += arr[i+j]
        
#   1. 최대값, 최소값 update (여기!!)
    
# 2.최대값, 최소값 위치는 어디?    
```



## 구현 (구간합.py)

``` python
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 최대값, 최소값 초기화
    max_value = 0
    min_value = 987654321

    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += arr[i + j]
        # 최대값/최소값 업데이트
        if max_value < total:
            max_value = total
        if min_value > total:
            min_value = total

    print(f'#{tc} {max_value - min_value}')
```



# 전기버스 (D2)

- 문제 :  [전기버스](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYIZDyM6218DFAV6&contestProbId=AYKKJeP6FIYDFAVG&probBoxId=AYJ_4ThKGR8DFAVG&type=USER&problemBoxTitle=08-09&problemBoxCnt=5)

- 완전 그리디 - 풀이 방법이 많다. 



## 설계

- 예시
  - 최대 이동 정류장 수 : 3
  - 정류장 수 :  0 ~ 10
  - 충전기 개수 :  5 ( 1, 3, 7, 8, 9 번 자리 )

| 정류장 (10)       |  0   |  1   | 2    |  3   |  4   |  5   |      6       |  7   |  8   | 9    |  10  |
| ----------------- | :--: | :--: | ---- | :--: | :--: | :--: | :----------: | :--: | :--: | ---- | :--: |
| 충전소 (5)        |      |  O   |      |  O   |      |      |              |  O   |  O   | O    |      |
| 마지막 충전 (3칸) | last |      |      | last |      |      | last (충전X) |      |      |      |      |
| 충전 횟수         |  0   |      |      |  1   |      |      |     실패     |      |      |      |      |



```python
for i : 1 → m+1
# 앞에꺼 전에꺼 비교
#   1번 경우 
    a[i] - a[i-1] > k # 못간다. 
#   2번 경우 
#   충전 불가 - 앞 충전소에서 충전해라
	a[i] > last + k
    → last = a[i+1]
      cnt += 1
```



## 구현 (전기버스.py)

```python
def f(arr, k, n, m):
    arr = [0] + arr + [n]   # 출발점과 도착점 추가
    last = 0    # 마지막으로 충전한 충전소 번호
    cnt = 0     # 충전 횟수

    for i in range(1, m + 2):
        # 충전기 사이가 K보다 크면 충전할 수 없음
        if arr[i] - arr[i-1] > k:
            return 0
        # 충전할 수 없는 경우 앞쪽에서 충전해야 함
        if arr[i] > last + k:
            last = arr[i-1]
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    # K = 최대이동횟수, N = 종점, M = 충전기 설치 위치
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {f(arr, K, N, M)}')
```



# Flatten (D3)

## 설계

```python
# 최대값의 인덱스
# 최소값의 인덱스
```



## 구현 (Flatten.py)

```python
T = 10
for tc in range(1, T+1):
    dump_count = int(input())
    N = 100
    arr = list(map(int, input().split()))

    for i in range(dump_count):
        # 최소/최대값의 인덱스
        max_idx = min_idx = 0
        for j in range(1, N):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[max_idx] -= 1
        arr[min_idx] += 1

        # 반드시 최종덤프후에 최고점과 최저점의 높이차를 반환
        max_idx = min_idx = 0
        for j in range(1, N):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j

    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')
```



## 구현 (Flatten함수.py)

```python
def min_max():
    max_idx = min_idx = 0
    for j in range(1, N):
        if arr[max_idx] < arr[j]:
            max_idx = j
        if arr[min_idx] > arr[j]:
            min_idx = j
    return max_idx, min_idx

T = 10
for tc in range(1, T+1):
    dump_count = int(input())
    N = 100
    arr = list(map(int, input().split()))

    for i in range(dump_count):
        # 최소/최대값의 인덱스
        max_idx, min_idx = min_max()

        arr[max_idx] -= 1
        arr[min_idx] += 1

        # 반드시 최종덤프후에 최고점과 최저점의 높이차를 반환
        max_idx, min_idx = min_max()

    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')
```

