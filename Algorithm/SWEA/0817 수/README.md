# 1215. 회문1

## 8x8 평면 글자판의 가로, 세로에 제시된 길이를 가진 회문의 총 개수 구하기

- 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말을 회문이라 한다.



1.  문자를 입력받아 8*8 행렬을 만든다
2.  각 행을 탐색하여 제시된 길이만큼 끊어 뒤집었을때 같은 리스트를 찾아 숫자를 센다.
3.  행과 열을 바꾼다.
4.  같은 방법으로 열이 바뀐 행을 탐색한다.



### Initial Code

```python
# 1
for tc in range(10):
    n = int(input())
    arr = []
    for s in range(8):
        abc = list(input())
        arr.append(abc)
# 2
    cnt = 0
    for i in range(8):  # 행 탐색
        for j in range(8-n+1):
            array = arr[i][j:j+n]     # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                cnt += 1

# 3
    for row in range(8):     # 행, 열 바꾸기
        for col in range(8):
            if row < col:
                arr[row][col], arr[col][row] = arr[col][row], arr[row][col]
# 4
    for i in range(8):  # 열 탐색
        for j in range(8-n+1):
            array = arr[i][j:j + n]
            if array == array[::-1]:
                cnt += 1

    print(f"#{tc+1} {cnt}")
```



- 2, 4번이 반복 시행되므로 함수로 만든다.

```python
# 각 행의 회문 개수를 구함
def palindrome(arr, n):
    cnt = 0
    for i in range(8):   # 행 탐색
        for j in range(8 - n + 1):
            array = arr[i][j:j + n]   # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                cnt += 1  # 같으면 숫자를 셈
    return cnt
```



- 3번을 zip 내장 함수를 사용하여 표현할 수 있다.

```python
# 행렬을 바꾸는 내장함수
arr =[[], [], []]     # 2차원 리스트
arr = list(zip(*arr)) # arr의 모든 요소의 행과 열을 바꿈
```



### final Code

```python
def palindrome(arr, n):  # 각 행의 회문 개수를 구하는 함수 생성
    cnt = 0
    for i in range(8):  # 행 탐색
        for j in range(8 - n + 1):
            array = arr[i][j:j + n]   # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                cnt += 1
    return cnt

for tc in range(10):
    n = int(input())
    arr = []
    for s in range(8):
        abc = list(input())
        arr.append(abc)

    palindrome1 = palindrome(arr, n) # 행 탐색

    # 행과 열 바꾸기 (내장함수 사용)
    arr = list(zip(*arr))

    palindrome2 = palindrome(arr, n) # 열 탐색

    print(f"#{tc+1} {palindrome1 + palindrome2}")
```



### Error (어려움)

```python
if arr[i][j:j+n] == arr[i][j+n-1:j-1:-1]
```

- 리스트의 슬라이싱 부분에서 error 발생 
  - `arr[i][4:-1:-1]` 이면 리스트의 인덱스 4에서 0 까지 [4, 3, 2, 1] 을 반환한다고 생각.
  - 하지만 [] 빈 리스트를 반환함



```python
arr = [1,2,3,4,5,6,7,8,9,10]

arr[4:0:-1] = [4,3,2]  # 인덱스 4 ~ 1까지 역순으로 출력

arr[4: :-1] = [4,3,2,1] # 인덱스 4 ~ 0까지 역순으로 출력

arr[4:-1:-1] = [] # [] 빈리스트 출력
```



### Error 수정

- 복잡해진다.

```python
for i in range(8):  # 열 탐색
    for j in range(8-n+1):
        if j == 0:
            if arr[i][:n] == arr[i][n-1::-1]:
                cnt += 1
        else:
            if arr[i][j:j+n] == arr[i][j+n-1:j-1:-1]:  # ex) 0에서 3 까지 == 3에서 0 까지
                cnt += 1
```



### 중요!

-  행과 열을 바꾸는 zip 내장 함수를 사용하여 표현
- 슬라이싱
  - `[4: :-1]` : 인덱스 4 ~ 0까지 역순
  - `[4:-1:-1]` : [] 빈리스트



# 1225. 암호생성기

## 주어진 사이클에 따라 조건을 만족하는 8자리의 암호를 생성하기

1.  반복 횟수를 모른다.
   - whlie 조건 반복문 사용
2.  5번씩 반복되는 사이클(빼는 수) 구하기
   - 5로 나눈 나머지를 이용
3.  처음 수를 마지막으로 옮길 방법
   - 슬라이싱과 `append`함수 이용
4.  if 문을 이용하여 값이 음수가 나오면 0으로 출력
5.  값에 0 이 나타나면 암호를 출력



### Code

```python
for t in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    cycle = 0 # 빼는수

    while 0 not in arr:
        cycle = (cycle % 5) + 1  # 빼는 수는 1-5까지 반복 (5로 나눈 나머지 +1)

        change = arr[0] - cycle # 처음 수에서 cycle을 뺀다.
        arr.append(change)      # 계산 된 수를 마지막에 추가해준다.
        arr = arr[1:]           # 처음 수를 제외한리스트를 담는다.

        if arr[7] < 0:
            arr[7] = 0
            break

    password = ' '.join(map(str, arr))
    print(f'#{tc} {password}')

# 같은 인덱스에 대해 반복 수행하므로 i에 대해 정의 할 필요없다.
```



### Error (어려움)

```python
i = i % 8 # 인덱스는 0에서 7까지 반복 (8로 나눈 나머지)
change = arr[i] - cycle

i += 1
```

- 처음 수를 뒤로 보내고 없애므로 같은 인덱스에 대해 계산을 계속한다.
  - 인덱스 i 에 대해 새롭게 정의해 줄 필요가 없다.



# 1220. Magnetic 

## 일정 간격을 두고 자기장을 걸었을 때, 자성체의 교착 상태 개수를 구하라.

- 1은 N극 성질, 2는 S극 성질
- 테이블의 윗부분에 N극이 아래부분에 S극이 위치한다.



1.  N극이 위, S극이 아래에 있다.
   -  자성체의 위치는 먼저 1(N극 성질)이 온 다음 2(S극 성질)가 와야 교착 상태가 된다.
2.  1,2가 붙었을 때 교착상태의 개수를 추가
   - 1이 먼저 오고 다음 2가 오면서 합이 3이 되면 교착 상태 개수 추가하는 코드로 구현



### Code

```python
for tc in range(10):
    n = int(input())
    arr = []
    for num in range(100):
        ns = list(map(int, input().split()))
        arr.append(ns)

# N극이 위, S극이 아래에 있으므로
# 자성체의 위치는 1(N극 성질)이 먼저 다음 2(S극 성질)가 와야 교착 상태가 된다.
# 1이 먼저 오고 다음 2가 오면서 합이 3이 되면 교착 상태 개수 추가
    cnt = 0
    for i in range(100):
        sum_ns = 0
        for j in range(100):
            if arr[j][i] == 1: # 각 열끼리 비교해야 하므로 열은 고정하고 행을 변화시킴
                sum_ns = 0     # 값이 1 이면 sum_ns 초기화

            sum_ns += arr[j][i] # 요소의 값을 계속 더 한다.

            if sum_ns == 3: # 합이 3이되면 교착상태 추가
                cnt += 1
                sum_ns = 0
    print(f'#{tc+1} {cnt}')
```



### Error (어려움)

```python
sum_ns = 0
```

- `sum_ns`의 초기화 위치 선정이 잘못됨
  - 초기 코드는  `cnt = 0`밑에 초기화 위치를 선정하여 값이 틀리게 나옴



# 2805. 농작물 수확하기 (리뷰)

## 농장 크기와 농작물 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익을 구하기

-  농장은 크기는 항상 홀수 (1 X 1, 3 X 3 … 49 X 49)
- 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능



1. 범위가 다른 각 배열의 합을 어떻게 구현할 지 생각
   - 중간 행을 기준으로 대칭으로 범위가 줄어든다.
     - 반틈만 규칙을 구하고 대칭시킨다
   - 중간 행을 기준으로 위아래로 범위를 하나씩 양쪽에서 줄여나가면서 더한다.



### Initial Code

```python
t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for num in range(n):
        profit = list(map(int, input()))
        arr.append(profit)
# 행렬의 중심을 기준으로 위아래로 범위를 양쪽에서 줄여나가면서 더한다.
    total = 0
    center = n//2
    for i in range(n//2+1):  # n//2 + 1 번 시행
        if i == 0:
            total += sum(arr[center])
        else:
            total += sum(arr[center-i][i:-i]) + sum(arr[center+i][i:-i])

    print(f'#{tc+1} {total}')
```



### 수정

- `total` 의 초기값을 `0`이 아닌 중간행 값으로 주면 `if - else `문이 필요없다.



### final Code

```python
t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for num in range(n):
        profit = list(map(int, input()))
        arr.append(profit)
# 행렬의 중심을 기준으로 위아래로 범위를 양쪽에서 줄여나가면서 더한다.
    center = n // 2
    total = sum(arr[center]) # 중간 행 따로 계산
    for i in range(1, n//2+1):  # n//2 + 1 번 시행
        total += sum(arr[center-i][i:-i]) + sum(arr[center+i][i:-i]) # 대칭하는 행을 한꺼번에 계산

    print(f'#{tc+1} {total}')
```





### Error (어려움)

- 수업시간에 배운 2차원 배열탐색을 이용하려다 오히려 코드가 어려워짐
- 어려워진 코드를 지우고 나만의 방법으로 새롭게 코드를 설계함



#  1234. 비밀번호

## 같은 번호로 붙어있는 쌍을 소거하고 남은 번호로 비밀번호 만들기

- 번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거
- 문자열은 0~9로 구성



1. 몇 개를 제거해야 하는 지 횟수를 알 수 없으므로 while 조건문 이용
2. 중간에 존재하는 같은 번호 쌍을 if 조건문을 사용하여 제거
3. 제거하고 남은 문자를 인덱스 앞뒤로 슬라이싱하여 빈 문자열에 추가 (새로운 배열 생성)
4. while 반복문을 멈추기 위한 조건 설정
   - 변수 생성
   - 처음 반복문이 실행될 때는 변수의 값을 변경 
   - 같은 문자가 연속으로 존재하면 처음 값과 같은 값을 주어 while 반복문이 실행되게 함
   - 같은 문자가 연속으로 존재하지 않으면 변경된 값을 유지하여 while의 실행 조건에 맞지 않으므로 while반복문 종료



### Code

```python
for tc in range(10):
    n, num = input().split()
    cnt = 1          # cnt 초기값 1
    while cnt != 0:  # cnt가 1이 아니면 계속 실행
        cnt = 0      # 반복문이 실행되면 cnt 값을 0으로 바꿔줌
        for i in range(len(num)-1):  # 아래서 연속된 수를 +1로 비교하므로 범위를 하나 줄여줌
            if num[i] == num[i+1]:   # 연속된 두개의 값이 같으면
                arr = ''
                arr += num[:i]    # 인덱스 전후의 값을 arr에 넣어줌
                arr += num[i+2:]
                cnt = 1  # 같은 값이 존재하면 cnt값을 1로 바꿈
                break
        num = arr # 같은 값을 지운 값으로 반복 시행 하므로 num값을 arr로 바꿔 반복 시행
        # 같은 값이 존재하지 않으면 cnt는 0이 되므로 반복문 종류

    print(f'#{tc+1} {num}')
```

```python
num = 1238099084

#1 12380084
#1 123884
#1 1234
#1 1234
```



- while 조건 True로 설정
- while문 내부에서 출력할 경우 마지막 시행이 두번 출력 되는 것을 방지함

```python
cnt = 1
while True:
    cnt = 0
    for i in range(len(num)-1):  # 아래서 연속된 수를 +1로 비교하므로 범위를 하나 줄여줌
        if num[i] == num[i+1]:
            arr = ''
            arr += num[:i]
            arr += num[i+2:]
            cnt = 1
            break
    if cnt == 0:
        break
    num = arr
    print(f'#{tc+1} {num}')
```

```python
num = 1238099084

#1 12380084
#1 123884
#1 1234
```



### Error (어려움)

```python
cnt = 1
while cnt != 0:
    # arr = ''                   # 마지막에 빈 공간 출력 위치 조정 필요
    cnt = 0
    for i in range(len(num)-1):  # 아래서 연속된 수를 +1로 비교하므로 범위를 하나 줄여줌
        if num[i] == num[i+1]:
            arr = ''             # 마지막에 빈공간을 포함하지 않기 위해 위치 조정
            arr += num[:i]
            arr += num[i+2:]
            cnt = 1
            break
    num = arr
print(f'#{tc+1} {num}')
```

```python
num = 1238099084

#1 12380084
#1 123884
#1 1234
#1                      : 마지막에 빈 공간 출력 - arr = '' 의 위치 조정이 필요
```

- `arr` 의 초기화 위치를 잘 못 선정하여 마지막에 빈문자열이 출력됨.
  - `print` 해보며 `arr` 의 초기화 위치를 잡음
  - if 문이 실행될 때 초기화



# 1244. 최대상금 (14/15  Fail) (보류) ★★★★★

## 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산하기

- 숫자판들 중에 두 개를 선택해 정해진 횟수만큼 위치 교환
- 반드시 횟수만큼 교환
- 동일한 위치의 교환이 중복 가능



### Code

```python
t = int(input())
for tc in range(t):
    array, num = input().split()
    num = int(num)
    arr = list(map(int, array))

    n = len(arr)
    repeat = 0
    i = 0
    while repeat < num:
        if i < len(arr):   # arr의 길이만큼 반복
            maxidx = i
            for j in range(n - 1, i, -1):
                if arr[maxidx] < arr[j]:  # 최대값 인덱스 찾기
                    maxidx = j
            arr[i], arr[maxidx] = arr[maxidx], arr[i]
        else:   # arr의 길이를 벗어나면 뒤에 두자리만 반복
            arr[-1], arr[-2] = arr[-2], arr[-1]

        if maxidx != i + 1:
            repeat += 1
        i += 1

    if 1 < num <= n//2:
        for k in range(num-1):
            if arr[k] == arr[k + 1]:
                a = n - 1 - k
                b = n - 2 - k
                if arr[a] > arr[b]:
                    arr[a], arr[b] = arr[b], arr[a]
    else:
        for k in range(n//2-1):
            if arr[k] == arr[k + 1]:
                a = n - 1 - k
                b = n - 2 - k
                if arr[a] > arr[b]:
                    arr[a], arr[b] = arr[b], arr[a]
    money = ''.join(map(str, arr))
    print(f'#{tc+1} {money}')

```



- 함수를 만들어 반복되는 것을 줄인다.

```python
def max_sort(arr, num): # arr배열, num 시행 횟수
    repeat = 0
    i = 0
    while repeat < num:
        if i < len(arr):
            maxidx = i
            for j in range(n-1, i, -1):
                if arr[maxidx] < arr[j]:  # 최대값 인덱스 찾기
                    maxidx = j
            arr[i], arr[maxidx] = arr[maxidx], arr[i]
        else: # arr의 길이를 벗어나면 뒤에 두자리만 반복
            arr[-1], arr[-2] = arr[-2], arr[-1]

        if maxidx != i+1:
            repeat += 1
        i += 1
    return arr

def same(arr, scale):
    for k in range(scale - 1):
        if arr[k] == arr[k + 1]:
            a = n - 1 - k
            b = n - 2 - k
            if arr[a] > arr[b]:
                arr[a], arr[b] = arr[b], arr[a]
    return arr

t = int(input())
for tc in range(t):
    array, num = input().split()
    num = int(num)
    arr = list(map(int, array))
    n = len(arr)

    arr = max_sort(arr, num) # 만든 함수 사용

    if 1 < num <= n//2:
        arr = same(arr, num)  # 만든 함수 사용
    else:
        arr = same(arr, n//2)
    money = ''.join(map(str, arr))
    print(f'#{tc+1} {money}')
```



### Error (어려움)

```python
 for k in range(num-1):
        if arr[k] == arr[k + 1]:
            a = n - 1 - k
            b = n - 2 - k
            if arr[a] > arr[b]:  
                arr[a], arr[b] = arr[b], arr[a]
```

- `if arr[a] > arr[b]`의 등호를 `>`로 잘못 표시
- 내림차순으로 정렬한 뒤 교환 횟수가 남아 있을 때 같은 숫자가 존재하면 같은 숫자끼리 교환