# 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
import sys
input = sys.stdin.readline

def binary_search(start, end):

    while start <= end:
        ssum = 0
        # 상한액
        mid = (start + end) // 2

        for money in budget:
            if mid <= money:
                ssum += mid
            else:
                ssum += money

        if ssum <= m:
            # 상한액 올려야 됌
            start = mid + 1
        else:
            # 상한액 내려야함
            end = mid - 1
    return end


n = int(input())
budget = list(map(int, input().split()))
# 총 예산
m = int(input())
start = 1
end = max(budget)
print(binary_search(start, end))