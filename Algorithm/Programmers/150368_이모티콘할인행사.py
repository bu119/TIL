# 1.이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 2.이모티콘 판매액을 최대한 늘리는 것.

def dfs(idx, m):
    global case, cases
    if idx == m:
        cases.append(case[:])
        return

    for z in [10, 20, 30, 40]:
        case[idx] = z
        dfs(idx + 1, m)
        case[idx] = 0

def solution(users, emoticons):
    global case, cases
    answer = [0, 0]
    # users = [비율, 가격]
    # 비율 이상의 할인 이모티콘 모두 구매
    # 가격 이상의 돈이 이모티콘 구매에 사용되면 모두 취소하고 서비스에 가입
    # emoticons : 정가
    n = len(users)
    m = len(emoticons)
    case = [0] * m
    cases = []

    # 할인률 경우의 수
    dfs(0, m)

    # 각 할인률 경우의 금액 계산
    for sale in cases:
        join = 0
        cost = [0] * n
        # 할인률 적용한 구매가능한 이모티콘 가격의 합
        for i in range(m):
            for j in range(n):
                per, maxprice = users[j]
                if sale[i] >= per:
                    cost[i] += emoticons[i] * (1 - sale[i] / 100)
        # 서비스 가입자 찾기
        for k in range(n):
            per, maxprice = users[k]
            if cost[k] >= maxprice:
                cost[k] = 0
                join += 1
        # 결과 갱신
        total = sum(cost)
        if answer[0] < join:
            answer = [join, total]
        elif total > answer[1]:
            answer[1] = total

    return answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))