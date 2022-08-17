# GNS (D3)

#### [S/W 문제해결 기본] 5일차

##  0~ 9가 섞여 있는 문자열을 작은 수부터 차례로 정렬하기

- "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"



1. 카운팅 이용



```python
digit = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    temp = input() 
    arr = list(map(str, input().split()))

    # 카운팅
    count = [0] * 10
    for item in arr:
        for j in range(10):
            if item == digit[j]:
                count[j] += 1

    # 출력
    print(f'#{tc}')
    for i in range(10):
        for j in range(count[i]):
            print(digit[i], end=' ')
    print()
```

