import sys

input = sys.stdin.readline
# 참가자 수
n = int(input())
# 각 대회의 점수 결과
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total = []

for i in range(n):
    total.append(A[i]+B[i]+C[i])


rankA = sorted(A, reverse=True)
rankB = sorted(B, reverse=True)
rankC = sorted(C, reverse=True)
rankT = sorted(total,reverse=True)


ans = [[],[],[],[]]

for j in range(n):
    ans[0].append(rankA.index(A[j])+1)
    ans[1].append(rankB.index(B[j]) + 1)
    ans[2].append(rankC.index(C[j]) + 1)
    ans[3].append(rankT.index(total[j]) + 1)

for k in ans:
    print(*k)