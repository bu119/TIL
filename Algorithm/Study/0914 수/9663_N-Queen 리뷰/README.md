# 9663. N-Queen

## N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기

- N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제

### JEA

- stack을 활용
- possible 함수로 가지치기
- n_queen 함수

```python
def possible(k):       # k행에서 퀸을 둘 수 있는 인덱스 리스트 반환
    temp = [0] * N
    if stack:
        for i, j in stack:
            for dj in [-1, 0, 1]:
                nj = j + dj * (k-i)     # k행에서 i번째 퀸의 공격 범위에 들어가는 인덱스
                if 0 <= nj < N:
                    temp[nj] = 1

    lst = []
    for i in range(N):
        if temp[i] == 0:        # 앞서 놓은 퀸들의 공격 범위에 들어가지 않는다면
            lst.append(i)
    return lst


def n_queen(k, cnt):
    global ans
    if cnt == N:
        ans += 1
        return
    else:
        possible_list = possible(k)
        for j in possible_list:
            stack.append([k, j])
            n_queen(k+1, cnt+1)
            stack.pop()


N = int(sys.stdin.readline())
ans = 0
stack = []      # 퀸을 놓는 위칫값을 담는 리스트
n_queen(0, 0)
print(ans)
```



### BU

- DFS를 judge함수로 가지치기
- judge 함수
  - 같은 열에 존재하는 지 확인
  - 새로운 퀸을 기준으로 대각선 위에 퀸이 존재하는 지 확인 
- dfs 함수
  - 마지막 행이 아니면
    - 해당 행에 각 열의 위치를 넣어보면서 judge 함수로 존재가능한 위치인지 판단
    - judge 함수를 통과하면 다음 행에 반복 시행
  - 마지막 행에 도달하면
    - 카운트 해주고 이전 dfs로 돌아감

```python
def judge(idx):                     # 퀸이 존재 가능한 위치인지 탐색
    for j in range(idx):            # 새로운 퀸의 공격 범위를 이미 존재하는 퀸의 위치와 비교
        if arr[j] == arr[idx]:      # 같은 열 탐색
            return 0
        elif idx - j == arr[idx] - arr[j] or idx - j == -(arr[idx] - arr[j]): # 대각선 탐색 (각 행과 열의 차이가 같으면 대각선에 존재)
            return 0
    return 1

def dfs(idx):                       # 행 번호
    global cnt
    if idx != n:                    # 마지막 행에 도착 안했을 때
        for i in range(n):          # 열 경우의 수
            arr[idx] = i
            if judge(idx):          # 현재 행의 가능한 열 위치가 존재하면
                dfs(idx+1)          # 다음 행의 열 위치 결정
    else:                           # 마지막 행에 도착하면
        cnt += 1                    # 카운트
        return

n = int(input())
arr = [0] * n           # 인덱스는 행, 원소는 열번호
cnt = 0
dfs(0)
print(cnt)
```

