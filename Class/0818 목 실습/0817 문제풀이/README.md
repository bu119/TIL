# 파스칼의 삼각형 (D2)

- 피보나치 수열로 함수를 만들어서 풀면  시간이 오래 걸려서 메모이제이션을 해야한다.



1. 전체 `10*10` 행렬을 만든다

2. 첫 번째 열과 대각선의 값은 모두 `1`이다.
3. 조합의 성질을 이용한다. `nCr + nCr+1 = n+1Cr`



### 설계

```python
size = 0
memo = [[0]*10 for _ in range(size)]
for i : 0 → size - 1
    for j : 0 → i
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
```



### 메모이제이션

```python
size = 100
memo = [[0] * 100 for _ in range(size)]

for i in range(size):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
print(memo[50][30])
```



### Code

```python
size = 100
memo = [[0] * 100 for _ in range(size)]

for i in range(size):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    print(f'#{tc}')

    for i in range(n):
        for j in range(i+1):
            print(memo[i][j], end=' ')
        print()
```

