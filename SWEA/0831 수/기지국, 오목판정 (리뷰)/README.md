#  기지국 (D3)

## 기지국에 커버 되지 않는 집의 수를 찾기

- 기지국은 세가지 종류가 있다. 
- 기지국이 위치한 원소는 ‘A’, ‘B’, ‘C’로 표시하며, 각각 동서남북으로 1, 2, 3개를 커버하는 기지국이다.
- 집이 위치한 원소는 ‘H’ 이다
- ‘X’인 원소는 아무 것도 없다는 것을 나타낸다.



### BU

- 4방향 탐색을 이용
- 기지국` A`, `B`, `C`와 각 기지국의 커버되는 개수를 셔너리의 키와 벨류로 표현
- 딕셔너리의 키를 만나면 
- 개수만큼 주변을 탐색해서 `H`이 있으면 `X`로 바꿈 
- `for문` 으로 남은 `H`의 개수 세기

```python
t = int(input())
for tc in range(t):
    n = int(input())
    space = [list(input()) for _ in range(n)]

    di = [0, 0, 1, -1]      # 동서남북
    dj = [1, -1, 0, 0]
    cnt = 0
    cover = {'A': 1, 'B': 2, 'C': 3}

    for i in range(n):
        for j in range(n):
            if space[i][j] in cover:
                for ch in range(1, cover[space[i][j]] + 1):    # 'C'이면 1,2,3 탐색
                    for k in range(4):
                        ci = i + di[k] * ch
                        cj = j + dj[k] * ch
                        if 0 <= ci < n and 0 <= cj < n:        # 벽 체크
                            if space[ci][cj] == 'H':           # H가 있으면
                                space[ci][cj] = 'X'            # X로 변경

    for i in range(n):
        for j in range(n):
            if space[i][j] == 'H':
                cnt += 1

    print(f'#{tc+1} {cnt}')
```



### SO

- 기지국 A, B, C일 때 거리를 포문으로 안하고 따로따로 해줌
- for문으로 돌렸으면 길이가 많이 줄었을 것 같다.

```python
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
 
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
 
    tower = [1, 2, 3]
 
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'
 
 
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                for m in range(1, 3):
                    for k in range(4):
                        ni = i + di[k] * m
                        nj = j + dj[k] * m
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'X'
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'C':
                for m in range(1, 4):
                    for k in range(4):
                        ni = i + di[k] * m
                        nj = j + dj[k] * m
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'X'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
 
    print(f'#{tc} {cnt}')
```



### JEA

- bu의 코드와 같은 데
- 다른 점은 벽체크 할 때 기지국도 생각해줘서 `X`로 변화 시키지 않은 점

```python
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    station = {"A": 1, "B": 2, "C": 3}

    for i in range(N):
        for j in range(N):
            if arr[i][j] in station:
                for d in range(4):
                    for k in range(1, station[arr[i][j]] + 1):
                        ni = i + di[d] * k
                        nj = j + dj[d] * k
                        if 0 <= ni < N and 0 <= nj <= N and arr[ni][nj] not in station:
                            arr[ni][nj] = "X"

    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "H":
                ans += 1

    print(f'#{tc} {ans}')
```



### YOON

- 소현이 코드 길이를 단축시킨 버전
- `H` 를 `X`로 변경하는 함수를 만들어서
- 각 기지국을 만났을 때 함수를 적용시킴

```python
def plus(M, i_idx, j_idx):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    arr[i_idx][j_idx] = 'X'
    for k in range(4):
        for m in range(1, 1+M):
            ni = i_idx + di[k] * m
            nj = j_idx + dj[k] * m
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'H':
                    arr[ni][nj] = 'X'
            else:
                break


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                plus(1, i, j)
            if arr[i][j] == 'B':
                plus(2, i, j)
            if arr[i][j] == 'C':
                plus(3, i, j)

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                count += 1

    print(f'#{tc} {count}')
```



# 오목 판정 (D3)

## 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하기

- 가로, 세로, 대각선 중 하나의 방향으로 5개 판정



### BU

- 5X5 행렬에서 오목을 판정하는 함수를 만듬
- 행렬을 5X5모양으로 잘라서 판정하고 나오면 break를 걸어줌

```python
def judge(arr):
    arr_col = list(zip(*arr))
    cnt_l = 0
    cnt_r = 0
    for r in range(5):
        # 행 탐색
        if arr[r].count('o') == 5:
            return 1
        # 열 탐색
        if arr_col[r].count('o') == 5:
            return 1
        # 대각선
        if arr[r][r] == 'o':
            cnt_l += 1

        if arr[r][4-r] == 'o':
            cnt_r += 1

        # 대각선 오목 탐색
    if cnt_l == 5 or cnt_r == 5:
        return 1
    else:
        return 0


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 0
    for i in range(n-5+1):
        for j in range(n-5+1):
            new_arr = arr[i:i + 5]
            for k in range(5):
                new_arr[k] = new_arr[k][j:j+5]   # 5x5로 자름

            result = judge(new_arr)
            if result == 1:
                break
        if result == 1:
            break

    if result == 1:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')
```



### SO

- 가로, 세로, 왼쪽 대각선, 오른쪽 대각선을 각각 판정

```python
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
 
 
    result = 0
 	# 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    result = 1
                    break
            elif arr[i][j] == '.':
                cnt = 0
 
 	# 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
                if cnt >= 5:
                    result = 1
                    break
            elif arr[j][i] == '.':
                cnt = 0
 
 	# 왼쪽 대각선
    for i in range(N - 5 + 1):  # 시작 좌표
        for j in range(N - 5 + 1):
            cnt = 0
            for k in range(5):
                if arr[k+i][k+j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        result = 1
                        break
                elif arr[k+i][k+j] == '.':
                    cnt = 0
 
 	# 오른쪽 대각선
    for i in range(N - 5 + 1):   # 시작 좌표
        for j in range(N - 1, 3, -1):
            cnt = 0
            for k in range(5):
                if arr[i+k][j-k] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        result = 1
                        break
                elif arr[i+k][j-k] == '.':
                    cnt = 0
 
    if result == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
```



### JEA

- 가로, 세로, 왼쪽 대각선, 오른쪽 대각선을 판정하는 함수를 만듬

```python
def check(arr):
    for i in range(N):
        cnt1 = cnt2 = 0
        for j in range(N):
            if arr[i][j] == 'o':            # 가로 탐색
                cnt1 += 1
            else:
                cnt1 = 0
            if arr[j][i] == 'o':            # 세로 탐색
                cnt2 += 1
            else:
                cnt2 = 0
            if cnt1 == 5 or cnt2 == 5:
                return "YES"

    for k in range(N-4):                    # 대각선 길이 최소 5
        cnt1 = cnt2 = 0
        for i in range(N-k):                  # 우하향 탐색
            if arr[i+k][i] == 'o':          # 중앙 대각선 기준 아래
                cnt1 += 1
            else:
                cnt1 = 0
            if arr[i][i+k] == 'o':          # 기준 위
                cnt2 += 1
            else:
                cnt2 = 0
            if cnt1 == 5 or cnt2 == 5:
                return "YES"

        cnt1 = cnt2 = 0
        for i in range(N-k):                  # 좌하향 탐색
            if arr[i+k][N-1-i] == 'o':      # 중앙 대각선 기준 아래
                cnt1 += 1
            else:
                cnt1 = 0
            if arr[i][N-1-i-k] == 'o':      # 기준 위
                cnt2 += 1
            else:
                cnt2 = 0
            if cnt1 == 5 or cnt2 == 5:
                return "YES"

    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(f'#{tc} {check(arr)}')
```



### YOON

- 가로, 세로, 왼쪽 대각선, 오른쪽 대각선을 판정하는 함수를 만듬

```python
def omok():
    for i in range(N): # 가로
        count = 0
        for j in range(N):
            if arr[i][j] == 'o':
                count += 1
                if count >= 5:
                    return 'YES'
            else:
                count = 0
    count = 0

    for i in range(N): # 세로
        count = 0
        for j in range(N):
            if arr[j][i] == 'o':
                count += 1
                if count >= 5:
                    return 'YES'
            else:
                count = 0
    count = 0

    for i in range(N-4): # 대각선
        for j in range(N-4):
            i_idx = i
            j_idx = j
            while 0 <= i_idx < N and 0 <= j_idx < N:
                if arr[i_idx][j_idx] == 'o':
                    count += 1
                    if count >= 5:
                        return 'YES'
                else:
                    count = 0
                i_idx += 1
                j_idx += 1

    count = 0

    for i in range(N-4): # 역대각선
        for j in range(N-4):
            i_idx = i
            j_idx = N-1-j
            while 0 <= i_idx < N and 0 <= j_idx < N:
                if arr[i_idx][j_idx] == 'o':
                    count += 1
                    if count >= 5:
                        return 'YES'
                else:
                    count = 0
                i_idx += 1
                j_idx -= 1

    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc} {omok()}')
```



### BU

- 2가지 방법으로 풀이함
- 아무도 안올린 방법이라 올림
- 4방향 탐색 이용해서 5개이면 break

```python
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 0
    # 4방향 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선 방향으로 탐색
    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    for size in range(5):
                        ci = i + di[k] * size
                        cj = j + dj[k] * size
                        if 0 <= ci < n and 0 <= cj < n and arr[ci][cj] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        result = 1
                        break
            if result:
                break
        if result:
            break

    if result:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')
```

