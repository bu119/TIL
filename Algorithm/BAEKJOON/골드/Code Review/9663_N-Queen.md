# 9663. N-Queen

## N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하기

#### [9663_N-Queen](https://www.acmicpc.net/problem/9663)

- N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

---

## Idea

- dfs , 백트래킹 활용하기 
- 새로운 퀸의 위치에서 이전 위치들을 공격하지 않는지 탐색
- 퀸은 한 행에 하나만 가능하므로 행을 인덱스로 주고 열을 원소로 갖는 배열 만들기
- 각 열과 대각선이 겹치지 않고 마지막해에 도착하면 카운트

---

## Problem

1. dfs를 활용한 백트레킹 구현이 어려움

2. 시간초과 (대각선 탐색 구현)

   - 시간이 오래걸리는 대각선 구하는 함수를 없애고 다른 방법 찾기

   ```python
   def diagonal(idx):                  	# 대각선 길 탐색
       dia = []
       for k in range(1, idx+1):           # 위쪽 대각선 탐색
           for d in [[-1, -1], [-1, 1]]:
               ni = idx + d[0] * k
               nj = arr[idx] + d[1] * k
               if 0 <= ni < n and 0 <= nj < n:
                   dia.append((ni,nj))
       return dia
   ```

---

## Revision

1. 백트래킹으로 가지치기

   ```python
   def judge(idx):                    				 # 퀸이 존재 가능한 위치인지 탐색
       for j in range(idx):           				 # 새로운 퀸의 공격 범위를 이미 존재하는 퀸의 위치와 비교
           if arr[j] == arr[idx]:     				 # 같은 열 탐색
               return 0
           elif abs(idx-j) == abs(arr[idx]-arr[j]): # 대각선 탐색 (각 행과 열의 차이가 같으면 대각선에 존재)
               return 0
       return 1
   ```

2. 대각선의 위치를 인덱스의 차만으로 판단

   ```python
   if abs(idx-j) == abs(arr[idx]-arr[j]): 			# 대각선 탐색 (각 행과 열의 차이가 같으면 대각선에 존재)
               return 0
   ```


---

## Code

```python
def judge(idx):                     # 퀸이 존재 가능한 위치인지 탐색
    for j in range(idx):            # 새로운 퀸의 공격 범위를 이미 존재하는 퀸의 위치와 비교
        if arr[j] == arr[idx]:      # 같은 열 탐색
            return 0
        elif abs(idx-j) == abs(arr[idx]-arr[j]): # 대각선 탐색 (각 행과 열의 차이가 같으면 대각선에 존재)
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

---

## Comment

- 문제를 읽고 **어떤 방법으로 알고리즘을 구현할지 생각하기!**
- dfs의 백트래킹 공부하기
