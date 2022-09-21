def cost(hill, low):
    cnt = [0] * n
    total = 0
    for i in range(n):
        if hill[i] < low:
            cnt[i] = low - hill[i]
        elif hill[i] > low + 17:
            cnt[i] = hill[i] - (low + 17)

    for j in cnt:
        total += j*j
    return total

n = int(input())
hill = [int(input()) for _ in range(n)]
hill.sort()

dif = (hill[n-1] - hill[0] - 17)
cost1 = cost2 = 0

if dif > 0:
    if dif % 1:
        low1 = hill[0] + (dif // 2) + 1
        cost1 = cost(hill, low1)

    low2 = hill[0] + (dif//2)
    cost2 = cost(hill, low2)

    if cost1:
        if cost1 < cost2:
            print(cost1)
        else:
            print(cost2)
    else:
        print(cost2)
else:
    print(0)
