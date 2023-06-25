n = int(input())
total = [0] * n
for i in range(3):
    competition = list(map(int, input().split()))

    # total 점수 더하기
    for j in range(n):
        total[j] += competition[j]

    rank = {}
    ans = []
    score = sorted(competition, reverse=True)
    for idx in range(n):
        if score[idx] not in rank:
            rank[score[idx]] = idx + 1
    for k in competition:
        ans.append(rank[k])

    print(*ans)

rank = {}
totalRank = []
score = sorted(total, reverse=True)
for idx in range(n):
    if score[idx] not in rank:
        rank[score[idx]] = idx + 1

for k in total:
    totalRank.append(rank[k])
print(*totalRank)