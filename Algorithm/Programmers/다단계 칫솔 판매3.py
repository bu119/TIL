def solution(enroll, referral, seller, amount):
    profits = [0] * len(enroll)
    member = {}
    for i, e in enumerate(enroll):
        member[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = member[s]
            profits[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return profits

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]

print(solution(enroll, referral, seller, amount))