t = int(input())
for tc in range(t):
    n = int(input())
    log = list(map(int, input().split()))
    log.sort()
    dif = 0
    for i in range(2, n):
        if dif < abs(log[i-2]-log[i]):
            dif = abs(log[i-2]-log[i])
    print(dif)