# 문자열 비교 (D2)

####  [파이썬 SW문제해결 기본 - String] 

## 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾기

### 설계

```python
n = 5 (문자열 길이)
m = 3 (패턴 길이)
p = 패턴
t = 문자열
for i : (n-m+1)
    flag = 1
    for j : (m)
        if t[i+j] != p[j]
        flag = 0
        break
    if flag:
        return 1
return 0
```



### Code

```python
def brute_force(p, t):
    for i in range(N - M + 1):
        flag = 1  # 참이라고 가정
        for j in range(M):
            if t[i + j] != p[j]:  # 인덱스 조절
                flag = 0
                break
        if flag:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    text = input()
    N = len(text)
    M = len(pattern)

    print(f'#{tc} {brute_force(pattern, text)}')
```



# 회문 (D2)

#### [파이썬 SW문제해결 기본 - String] 

##  길이가 M인 회문을 찾아 출력하기

- 행 방향을 회문을 구한다.
- 열 방향은 인덱스만  변경해준다.
- 정방 행렬일 때 행과열의 인덱스 위치만 바꿔서 풀이할 수 있다.
- zip 함수 써도 됩니다.



### 설계

```python
for i : 0 → n-1
    for j : 0 → n-m                            # 까지 돌아야한다.
        flag = 1
        for k : 0 → m//2-1
            if arr[i][j+k] != arr[i][j+m-1-k]: # j+m-1 맨뒤 인덱스 - k
                flag = 0
                break                          # 다르면 빠져나온다.
        if flag:
            for k : 0 → m//2-1                 # k 만큼 돈다.   
                print(arr[i][j+k])
```

 

### Code

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
 
    print(f'#{tc}', end=' ')
    # 행방향
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M // 2):
                if arr[i][j+k] != arr[i][j + M - 1 -k]:
                    flag = 0
                    break
            # 출력
            if flag:
                for k in range(M):
                    print(f'{arr[i][j+k]}', end='')
                print()
 
    # 열방향
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M // 2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    flag = 0
                    break
            # 출력
            if flag:
                for k in range(M):
                    print(f'{arr[j+k][i]}', end='')
                print()
```



# 글자수 (D3)

#### [파이썬 SW문제해결 기본 - String] 

## 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,

## 그중 가장 많은 글자의 개수를 출력하기

### Code

```python
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
 
    # dict 초기화
    my_dict = {}
    # dict를 이용해서 중복제거
    for key in set(str1):
        my_dict[key] = 0
 
    # 카운팅
    for key in str2:
        if key in my_dict:
            my_dict[key] += 1
 
    # 최대값
    ans = 0
    for value in my_dict.values():
        if ans < value:
            ans = value
 
    print(f'#{tc} {ans}')
```



# 가장 빠른 문자열 타이핑 (D4)

## A를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하기

- 길이 만큼 건너 뛰어야함
- 슬라이싱이 독이 될 수 있다.

```python
aaaa aa # 2
```



## fail

- i 값을 조정해야 하므로 for문으로 안된다.
- for문을 while문으로 변경

```python
T = int(input())
for tc in range(1, T + 1):
    text, pattern = map(int, input().split())
    n = len(text)
    m = len(pattern)
    cnt = 0
    for i in range(n-m+1):
        flag = 1
        for j in range(m):
            if text[i+j] != pattern[j]:
                flag = 0
                break
        if flag:
            cnt += 1
    print(f'#{tc} {n - m * cnt + cnt}')
```



### Code

```python
T = int(input())
for tc in range(1, T+1):
    text, pattern = map(str, input().split())
    N = len(text)
    M = len(pattern)

    cnt = 0
    i = 0
    while i < N-M+1:
        flag = 1
        for j in range(M):
            if text[i+j] != pattern[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i = i + M - 1   # i가 패턴길이만큼 이동
        i += 1

    print(f'#{tc} {N - M * cnt + cnt}')
```



# 회문2 (D3)

#### [S/W 문제해결 기본] 3일차

## 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하기

### Code

```python
def f(arr):
    M = 100   # 회문 최대 길이
 
    while M > 0:
        # 행방향
        for i in range(N):
            for j in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[i][j + k] != arr[i][j + M - 1 - k]:
                        flag = 0
                        break
                # 출력
                if flag:
                    return M
 
        # 열방향
        for i in range(N):
            for j in range(N - M + 1):
                flag = 1
                for k in range(M // 2):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        flag = 0
                        break
                # 출력
                if flag:
                    return M
        M -= 1
 
T = 10
for tc in range(1, T+1):
    N = 100
    no = int(input())
    arr = [list(input()) for _ in range(N)]
 
    print(f'#{tc} {f(arr)}')
```

