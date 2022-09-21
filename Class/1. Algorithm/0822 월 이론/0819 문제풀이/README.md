# 파리 퇴치 (D2)

## N x N 배열 안에 M x M 크기의 파리채로 죽인 최대 파리 개수 구하기

- for문 4개 필요
  - 밖에 정사각형
  - 안에 정사각형



### 수도코드

```python
 for i : (N-M+1)
        for j : (N-M+1)
            sum_v = 0
            for ii : (M)
                for jj : (M)
                    sum_value += arr[i+ii][j+jj]
            if max_va< sum_v
                max_v = sum_v
```



### Code

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_value = 0
            for ii in range(M):
                for jj in range(M):
                    sum_value += arr[i+ii][j+jj]
            if max_value < sum_value:
                max_value = sum_value
    print(f'#{tc} {max_value}')
```





# 어디에 단어가 들어갈 수 있을까 (D2)

## N X N 크기 퍼즐에 길이 K를 갖는 단어가 들어갈 수 있는 자리의 개수 구하기

- 가로, 세로 모두 탐색



### 수도 코드

```python
ans = 0
for i : (N)
        cnt = 0
        for j : (N)
            if arr[i][j] == 1:      # 1일 때
                cnt += 1
            else:                   # 0일 때
                if cnt == K:
                    ans += 1
                cnt = 0
    
        if cnt == K:                # 마지막 값이 1일 때 체크
            ans += 1
```



### Code

```python
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 행방향
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:      # 1일 때
                cnt += 1
            else:                   # 0일 때
                if cnt == K:
                    ans += 1
                cnt = 0
        # 마지막 값이 1일 때 체크
        if cnt == K:
            ans += 1

    # 열방향
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:      # 1일 때
                cnt += 1
            else:                   # 0일 때
                if cnt == K:
                    ans += 1
                cnt = 0
        # 마지막 값이 1일 때 체크
        if cnt == K:
            ans += 1

    print(f'#{tc} {ans}')
```

