n = int(input())
hill = [int(input()) for _ in range(n)]
cnt = [0] * n
cost = 0
hill.sort()
# print(hill)
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
# print(cnt)
# print(hill)
print(cost)