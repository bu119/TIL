# 9881. Ski Course Design

## 언덕의 높이를 x 단위로 변경하는 데 지불해야 하는 최소 금액 구하기

#### [9881. Ski Course Design](https://www.acmicpc.net/problem/9881)

- 가장 높은 언덕과 가장 낮은 언덕 사이의 차이가 엄격하게 17보다 크면 세금 부과
- 가장 높은 언덕을 줄이고 짧은 언덕의 높이를 높이면 가장 높은 언덕과 가장 낮은 언덕 사이의 새 차이가 최대 17인 한 세금을 내지 않을 수 있다.
- 언덕의 높이를 x 단위로 변경하는 데 x^2 단위의 돈이 든다.

---

## Idea

- 산의 최대 높이 보다 낮은 모든 높이를 고려하여 완전 탐색 (그리디 실패)
- 주어진 산의 높이 이외의 높이도 모두 고려하여 최소비용을 찾아야 한다. 

---

## Problem

1. 주어진  산의 높이만 고려하여 코드를 구현했기 때문에 testcase 만 통과함
2. 완전 탐색으로 할 경우 시간초과가 날 것이라 판단하고 조건을 달아 그리디하게 구현 
3. 그리디로 구현하기 실패 → 완전 탐색


---

## Revision

1. 최대 높이 전까지의 모든 높이를 최소 높이로 잡고 구현한다.

2. 완전 탐색에서 시간 초과가 나지않음

   ```python
   cost = [0] * (hills[-1])        # 인덱스가 최소 높이
   
   for low in range(hills[-1]):    # 각 인덱스를 최소 높이로 탐색
       cnt = 0                     # 비용
       for j in range(n):
           num = hills[j]          # 비교할 숫자
           high = low + 17         # 최대 높이
   ```

---

## Code (완전탐색)

```python
n = int(input())
hills = [int(input()) for _ in range(n)]
hills.sort()

cost = [0] * (hills[-1])        # 인덱스가 최소 높이

for low in range(hills[-1]):    # 각 인덱스를 최소 높이로 탐색
    cnt = 0                     # 비용
    for j in range(n):
        num = hills[j]          # 비교할 숫자
        high = low + 17         # 최대 높이
        if num < low:
            cnt += (low - num) ** 2
        elif num > high:
            cnt += (num - high) ** 2
    cost[low] = cnt

print(min(cost))
```

### Fail Code (그리디)

```python
n = int(input())
hill = [int(input()) for _ in range(n)]
cnt = [0] * n
cost = 0
hill.sort()

dif = hill[n-1] - hill[0] - 17

if dif > 0:
    low = hill[0] + dif//2
    high = hill[n - 1] - dif//2
    cnt[0] = cnt[n - 1] = dif // 2
    if dif % 2:
        if low < hill[1]:
            low += 1
            cnt[0] += 1
        else:
            high -= 1
            cnt[n - 1] += 1

    for i in range(1, n):
        if hill[i] < low:
            cnt[i] = (low - hill[i])
        elif high < hill[i]:
            cnt[i] = (hill[i] - high)

    for i in cnt:
        cost += i*i

print(cost)
```

---

## Comment

- **그리디로 구현하지말고 완전탐색하자!**
- **시간초과가 난다면 가치지기로 백트레킹!**

