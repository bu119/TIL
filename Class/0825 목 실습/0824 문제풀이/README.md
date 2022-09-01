# 암호생성기 (D3)

#### [S/W 문제해결 기본] 7일차

## 주어진 조건에 따라  8자리의 암호를 생성하기

- 8개의 숫자
- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
- 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 
- 그 다음 수는 4, 그 다음 수는 5를 감소한다.
- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다.



### Code

```python
T = 10
for tc in range(1, T + 1):
    no = int(input())
    Q = list(map(int, input().split()))

    count = 0
    temp = 0

    while True:
        temp = Q.pop(0)
        temp -= count % 5 + 1
        if temp < 0: temp = 0

        Q.append(temp)
        count += 1
        if temp == 0:
            break

    print("#{}".format(tc), end=" ")
    for i in range(len(Q)):
        print(Q[i], end=" ")
    print()
```

