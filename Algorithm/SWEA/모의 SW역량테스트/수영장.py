t = int(input())
for tc in range(t):
    fee = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    expense = [0]*13                                                    # 인덱스 12달

    for i in range(1, 13):
        expense[i] = min(plan[i] * fee[0], fee[1]) + expense[i-1]       # 1일, 1달 이용권 비교

        if i > 2:                                                       # 3월부터
            expense[i] = min(expense[i], fee[2] + expense[i-3])         # 3달 이용권 비교

    ans = min(expense[12], fee[3])                                      # 1년 이용권 비교
    print(f'#{tc+1} {ans}')


'''
T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    expense = [0 for _ in range(13)]

    for i in range(1, 13):
        # 하루, 한달 비교
        expense[i] = min(plan[i] * price[0], price[1]) + expense[i-1]
        # 3개월 이상부터 3달까지 비교
        if i > 2:
            expense[i] = min(expense[i], price[2] + expense[i-3])
    # 1년 비교
    ans = min(expense[12], price[3])
    print(f'#{tc} {ans}')
'''