from itertools import combinations
arr = [int(input()) for _ in range(9)]

C = list(combinations(arr, 7))  # 조합 함수 사용

CC = []
for i in range(len(C)):
    if sum(C[i]) == 100:
        CC = sorted(C[i])

for i in range(len(CC)):
    print(CC[i])