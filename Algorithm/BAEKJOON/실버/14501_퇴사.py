def pro(date):
    global total

    day = date + schedule[date][0]

    if day <= n:
        total += schedule[date][1]
        if day < n:
            pro(day)
    else:
        return


def profit(date, p):
    global ans

    if date > n:
        return

    if ans < p:
        ans = p

    day = date + schedule[date][0]
    for x in range(day, n-day):
        if day + x <= n:
            profit(date + schedule[day+x][0], p + schedule[date][1])




n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
ans = 0

ans2 = 0

profit(0, 0)

for i in range(n):
    total = 0
    pro(i)
    if ans2 < total:
        ans2 = total

print(ans)
print(ans2)

