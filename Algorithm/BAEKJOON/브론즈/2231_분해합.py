n = int(input())
ans = 0
for i in range(1, 1000001):
    num = str(i)
    ssum = i
    for j in num:
        ssum += int(j)

    if ssum == n:
        ans = i
        break

print(ans)