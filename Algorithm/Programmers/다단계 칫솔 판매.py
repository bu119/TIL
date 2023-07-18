from collections import deque

def distribute(start, profit):
    global answer, memberIdx, graph, n

    deq = deque()
    deq.append((start, profit))
    # stack = [(start, profit)]

    while deq:
        v, money = deq.popleft()
        # v, money = stack.pop()

        commission = money // 10
        if commission < 1:
            commission = 0
            myProfit = money
        else:
            myProfit = money - commission

        answer[v] += myProfit
        if commission != 0 and graph[v] != n:
            # stack.append[(graph[v],commission)]
            deq.append((graph[v], commission))


def solution(enroll, referral, seller, amount):
    global answer, memberIdx, graph, n

    n = len(enroll)
    # emroll의 인덱스에 따라 멤버 이름 저장
    # 이름으로 인덱스 찾기 가능
    memberIdx = {}
    for i in range(n):
        memberIdx[enroll[i]] = i
    memberIdx['center'] = n

    # 수익 저장
    answer = [0] * (n + 1)

    # 민호는 n 번째 사람
    graph = [n] * (n + 1)

    # 그래프 관계 (데려온 사람 번호)
    for j in range(n):
        if referral[j] == '-':
            graph[j] = n
            continue
        graph[j] = memberIdx[referral[j]]

    m = len(seller)
    # 수익 계산
    for k in range(m):
        earnings = amount[k] * 100
        distribute(memberIdx[seller[k]], earnings)

    return answer[:-1]


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]

print(solution(enroll, referral, seller, amount))