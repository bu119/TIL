def profit(day, p):
    global ans

    if day > n:         # 퇴사일 넘음
        return
    else:               # 퇴사일 포함
        if ans < p:     # 수익이 더 크면
            ans = p
        if day == n:    # 퇴사일
            return

    profit(day + schedule[day][0], p + schedule[day][1])    # 날짜 선택
    profit(day + 1, p)                                      # 날짜 선택 안함


n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

ans = 0
profit(0, 0)
print(ans)