# 1986. 지그재그 숫자
t = int(input())
for i in range(t):
    n =  int(input())
    total = 0
    for j in range(1, n+1):
        if j % 2:
            total += j
        else:
            total -= j
    print(f'#{i+1} {total}')