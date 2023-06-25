# 참가자 수
n = int(input())
# 각 대회의 점수 결과
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total = []
for i in range(n):
    total.append(A[i]+B[i]+C[i])

ans = [[],[],[],[]]

for i in range(n):
    rankA, rankB, rankC, rankT = 1, 1, 1, 1
    # 모든 요소와 비교하여 작으면 1 더한다
    for j in range(n):
        if A[i] < A[j]:
            rankA += 1
        if B[i] < B[j]:
            rankB += 1
        if C[i] < C[j]:
            rankC += 1
        if total[i] < total[j]:
            rankT += 1
    ans[0].append(rankA)
    ans[1].append(rankB)
    ans[2].append(rankC)
    ans[3].append(rankT)

for k in ans:
    print(*k)
