# 1859. 백만 장자 프로젝트
# 최대값을 찾아 최대값 전 까지 수를 다더하고 최대값 * 개수 - 구매한수 더한다. 다음
#
import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    max_p = max(price)
    profit = 0

    #1

    for i in range(n):
        if price[i] < max_p:   # 최대값보다 작으면
            profit += max_p - price[i]     # 최대값과 매매가의 차이를 이익에 더함
        elif i + 1 < n:
            m = price[i + 1:]
            max_p = max(m)     # 이후 범위 부터 최대값 재설정
    print(f'#{tc + 1} {profit}')

    #2

    #     else:  # 최대값과 같으면
    #         idx = i  # 최대값의 인덱스를 넣어주고
    #         if idx + 1 < n:
    #             m = price[idx + 1:]
    #             max_p = max(m)  # 이후 범위 부터 최대값 재설정
    # print(f'#{tc + 1} {profit}')

# for i in range(n):
    #     if price[i] < max_p:   # 최대값보다 작으면
    #         buy += price[i]    # 구매하여 매매가를 더하고
    #         cnt += 1           # 구매 개수를 세어라
    #     else:                  # 최대값과 같으면
    #         idx = i            # 최대값의 인덱스를 넣어주고
    #         profit += cnt * price[idx] - buy      # 여기 까지 이익 계산
    #         buy = 0     # 0으로 재설정
    #         cnt = 0
    #
    #         if idx + 1 < n:
    #             m = price[idx+1:]
    #             max_p = max(m)  # 이후 범위 부터 최대값 재설정
    #
    # print(f'#{tc+1} {profit}')