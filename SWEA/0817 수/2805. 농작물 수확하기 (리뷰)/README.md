# 2805. 농작물 수확하기 (리뷰)

### 농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익구하기

-  N X N크기의 농장
-  농장은 크기는 항상 홀수 (1 X 1, 3 X 3 … 49 X 49)
-  수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능



![image-20220817134536135](C:\Users\LG\AppData\Roaming\Typora\typora-user-images\image-20220817134536135.png)



## 리뷰

- 부경, 윤경, 재건 비슷 방법으로 문제 해결 (중심 따로 해결)
  - 중간 행의 합을 따로 구해줌
  - 나머지 행의 합을 구해줌
  - 차이점
    - 부경: 안쪽에서 밖으로 더해 나감
    - 윤경: 밖에서 안으로 더해 나감
    - 재건: 중간행을 기준으로 위아래 나눠 계산 



- 소현 
  - 전부 순서대로 위래서 아래로 행을 이동하면서 더함
  - 행의 범위에 따라 열의 범위를 더하기 빼기로 조정
  - 새로움



## BU

```python
def add(arr): # sum함수 대신 사용
    sum_arr = 0
    for i in arr:
        sum_arr += i
    return sum_arr

t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for num in range(n):
        profit = list(map(int, input()))
        arr.append(profit)
# 행렬의 중심을 기준으로 위아래로 범위를 양쪽에서 줄여나가면서 더한다.
    center = n // 2
    total = add(arr[center]) # 중간 행의 값을 넣어줌
    for i in range(n//2+1):  # n//2 + 1 번 시행
        total += add(arr[center-i][i:-i]) + add(arr[center+i][i:-i]) # 대칭하는 행을 한꺼번에 계산
    print(f'#{tc+1} {total}')
```



## YOON

``` python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [] # 2차원 배열 입력받기
    for n in range(N):
        arr.append(list(map(int, input())))

    d = N//2 # N의 중간값
    total = sum(arr[d]) # 농작물 수익    # 중간행 따로 구함

    for i in range(d): # 끝에서 부터 안쪽으로 더해줌
        temp1 = arr[i][d-i : d+1+i] # 슬라이싱 할 때 원하는 숫자보다 1더해줘야한다
        temp2 = arr[N-1-i][d-i : d+1+i]
        total += sum(temp1) + sum(temp2)

    print(f'#{tc} {total}')
```



## JEA

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 2차원 배열
    mid = N // 2
    total = 0

    # 윗줄에서 아랫줄로 순차적으로 더하기
    # 중간행 위에 행
    for i in range(mid): #[0,1,...,mid-1]
        for j in range(mid - i, mid + i + 1): # 열이 i에 따라 범위가 늘어남
            total += arr[i][j]
    # 중간 행
    for i in range(N):
        total += arr[mid][i]

    # 중간행 아래행
    for i in range(1, mid + 1): #행 : [1,...,mid]
        for j in range(i, N - i): # i에 따라 한칸씩 범위가 줄어듬 
            total += arr[mid + i][j]  #행 : [1+mid,...,mid+mid]

    print(f'#{tc} {total}')
```



## SO

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 2차원 배열

    result = 0
    JS = N // 2 # 중간 행
    JE = N // 2 # 중간 행
    print(list(range(N)))
    for i in range(N):
        print(list(range(JS, JE + 1)))
        for j in range(JS, JE + 1):  # 중간 인덱스를 기준으로 열 범위 변화
            print(i,j)
            result += arr[i][j]

        if i < N // 2:  # 중간행 위에 행들은 내려오면서 열의 범위가 커짐
            JS -= 1
            JE += 1
        else:           # 중간행 아래 행들은 내려오면서 커졌던 열의 범위가 작아짐
            JS += 1
            JE -= 1

    print(f'#{tc} {result}')
```



- 중간행을 먼저 계산 하고 하면 for문 하나로 문제를 해결할 수 있어서 좀 더 간단하다.