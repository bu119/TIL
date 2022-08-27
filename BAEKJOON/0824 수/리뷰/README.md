# 방배정 (13300)

## 1학년부터 6학년까지 학생들이 묵을 방을 배정하기

- 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정
- 한 방에는 같은 학년의 학생들을 배정



###  Yoon

- 6개의 학년이 있어서 인덱스 6까지 빈 배열을 만듬
- 빈배열에 성별과 학년 별로 카운트함
- total 로 방 개수를 셈
- 나머지가 있으면 방하나를 추가

```python
N, K = map(int, input().split())
arr = [[0]*7, [0]*7]    # 학년 인덱스 빈 배열
for _ in range(N):
    sex, num = map(int, input().split())
    arr[sex][num] += 1

total = 0
for i in range(2):
    for j in range(1, 7):
        total += arr[i][j]//K
        if arr[i][j] % K:
            total += 1
print(total)
```



### Jea

- 딕셔너리 사용
- 튜플 형태로 (성별, 학년) 을 키로 두고 같으면 카운트 해줌
- 카운트한 값이 배정 인원 수보다 크면 몫을 더해주고 나머지가 있으면 1을 더해주고
- 같거나 작으면 1만 더하는 방식
- 딕셔너리에 키로 받은 것이 다르다.



#### Code

```python
import sys

N, K = map(int, sys.stdin.readline().split())

student_dict = {}
for i in range(N):
    student = tuple(sys.stdin.readline().split())
    if student in student_dict:
        student_dict[student] += 1
    else:
        student_dict[student] = 1

ans = 0
for value in student_dict.values():
    if value > K:
        ans += (value // K)
        if value % K:
            ans += 1
    else:
        ans += 1

print(ans)
```



### So

- 특이해서 리뷰하기 어려움
- `room`이라는 배열에 `[1학년 [ 남자, 여자 ] , 2학년 [ 남자, 여자 ], ... , 6학년 [ 남자, 여자 ]]`
- 각 학년의 남녀 수를 세서 배정인원 보다 작거나 같으면 1 추가
- **정원을 초과할 때 오류가 있다.**
- 배정인원으로 나눈 몫에 무조건 1 추가함
- 케이스가 다 홀수로 끝나서 통과됨
- 인원이 `4`거나 `6`인 짝수 케이스가 있었으면 통과 못함



#### Code

```python
# 일단 2점 받아서 추후 수정
N, K = map(int, input().split())
room = [[[],[]] for _ in range(7)] # 빈방 구현

for _ in range(N):
    s, y = map(int, input().split())
    room[y][s].append(1) # 학년 y, 성별 s
# 방에 학년과 성별에 맞춰 배치
'''
[
[[], []],             인덱스 0 이라 아무것도 없음. 
[[1], [1, 1]],        1학년 [ 남자, 여자 ] 
[[1, 1], [1]],        2학년 [ 남자, 여자 ]
[[1], [1, 1, 1]],     3학년
[[], [1]],
[[1], [1, 1]],
[[1], [1]]            6학년
]
'''
cnt = 0
for i in range(1, 7):
    for j in range(2):
        # 정원이 성립할 때  # 배정인원 보다 작거나 같으면 1 추가
        if len(room[i][j]) <= K and len(room[i][j]) > 0:
            cnt += 1
        # 정원을 초과할 때  # 각 배정인원 보다 크면 몫에 1 추가
        elif len(room[i][j]) > K:
            cnt += len(room[i][j]) // K + 1
            
         # 오류
         # len(room[i][j]) // K + 1
         # 4명인 경우 틀림

print(cnt)
```



### Bu

- 윤경이랑 같은 방식



#### Code

```python
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
boy = [0] * 7                  # 학년 별 인덱스
girl = [0] * 7
for i in range(n):
    if arr[i][0]:              # 남
        boy[arr[i][1]] += 1
    else:                      # 여
        girl[arr[i][1]] += 1
cnt = 0
for j in range(7):
    if boy[j] % m:             # 나머지 있으면
        cnt += boy[j]//m + 1   # 몫에 +1
    else:
        cnt += boy[j] // m

    if girl[j] % m:
        cnt += girl[j]//m + 1
    else:
        cnt += girl[j] // m

print(cnt)
```



# 일곱 난쟁이 (2309)

## 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이를 찾기

- 일곱 난쟁이 키의 합이 100



### Yoon

- `9명 키의 합 - 100` 으로 초과하는 키 크기를 구함
- for 문으로 합이 초과하는 크기인 난쟁이 2명 찾기
- 9명중에서 2명을 골라 둘이 합쳐서 초과하는 크기가 나오면
- 2명을 뺀 나머지 인원을 result에 추가함
- sorted로 정렬해서 프린트



#### Code

```python
arr = []
for i in range(9):
    arr.append(int(input()))

result = []
test = sum(arr)-100  # 9명키의 합 - 100 # 초과하는 크기를 구함
# 합이 초과하는 크기인 난쟁이 2명 찾기
for i in range(9):
    for j in range(9):
        # i,j 가 다르고 둘이 합쳐서 초과하는 크기가 나오면
        # 두명을 뺀 나머지 인원을 result에 추가함
        if test - arr[i] == arr[j] and i != j:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    result.append(arr[k])
            break
    if len(result):
        break
# sorted로 정렬해서 프린트
for r in sorted(result):
    print(r)
```



### Jea

- 키로 이루어진 리스트를 만듬
- combinations이 조합을 구하는 함수 (리스트에 있는 값들의 모든 조합)
- `combinations(N, 7)` 을 사용하여 N명 중에 7명을 뽑은 경우의 수를 list에 넣음
- for문으로 합이 100인 리스트를 찾아
- `sorted`로 오름차순으로 정렬하고 프린트



#### Code

```python
import sys
from itertools import combinations

N = []
for i in range(9):
    N += [int(sys.stdin.readline())]
# 키로 이루어진 리스트를 만듬
# combinations이 조합을 구하는 함수 (리스트에 있는 값들의 모든 조합을 구함)
# N명 중에 7을 뽑은 경우의 수를 list에 넣음
temp = list(combinations(N, 7))
for dwarf in temp:
    if sum(dwarf) == 100:   # 합이 100인 리스트를 찾아
        dwarf = sorted(list(dwarf))  # 오름차순으로 정렬하고
        print(*dwarf, sep='\n')      # 프린트
        break
```

- combinations이 함수로 있는 지 몰랐는데 알게 됌



### So

- combinations 함수를 사용해서
- for문으로 돌려서 합이 100이 되는 배열을 찾고
- sorted로 정렬해서 프린트



#### Code

```python
from itertools import combinations
arr = [int(input()) for _ in range(9)]

C = list(combinations(arr, 7))  # 조합 함수 사용

CC = []
for i in range(len(C)):
    if sum(C[i]) == 100:
        CC = sorted(C[i])

for i in range(len(CC)):
    print(CC[i])
```



### Bu

- 키를 height 배열에 추가
- sort함수로 미리 정렬
- `first = 0` 은 밑에서 for문 돌리는 횟수를 줄이려고 만듬
- for문을 활용하여 9명의 키를 다 더한 값에서 두명의 키를 빼고
- 100이 나오면 그 때 2명의 인덱스를 first, second에 넣어줌
- pop()함수 를 활용하여 인덱스에 맞는 값 제거
- second 인덱스가 first인덱스 보다 뒤에 있는데 앞에 pop으로 뒤에 인덱스가 감소 했기 때문에 `second -1` 해줌 



#### Code

```python
height = []
for n in range(9):
    height.append(int(input()))
# height에 키를 list로 추가
# 미리 정렬
height.sort()
# 밑에서 for문 돌리는 횟수를 줄이려고 만듬
first = 0
# for문을 활용하여 9명의 키를 다 더한 값에서 두명을 빼고
# 100이 나오면 그때 2명의 인덱스를 first, second에 넣어줌
for i in range(8):
    for j in range(i+1, 9):
        if sum(height) - height[i] - height[j] == 100:
            first = i
            second = j
            break
    # first에 값이 있으면 포문 나옴
    if first:
        break
# pop(인덱스)를 활용하여 제거
height.pop(first)
# second 인덱스가 first인덱스 보다 뒤에 있어서
# 앞에 pop으로 뒤에 인덱스가 감소 했기 때문에 -1 해줌 
height.pop(second-1)
for k in height:
    print(k)
```

