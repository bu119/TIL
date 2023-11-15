# 심리적인 거리는 두 사람의 MBTI 유형에서 서로 다른 분류에 속하는 척도의 수
# ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP, ESTJ, ESFJ, ENFJ, ENTJ
from itertools import combinations
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()

    # 사람 수가 32이상이면 같은 mbti가 무조건 3개이상 존재
    if n > 32:
        print(0)
        continue

    minV = 13
    # mbti 3개 선택
    for case in set(combinations(mbti, 3)):
        c1, c2, c3 = map(set, case)
        # 3개 중 2개씩 선택
        dist = 4 - len(c1 & c2)
        dist += 4 - len(c1 & c3)
        dist += 4 - len(c2 & c3)
        # 최솟값 비교
        minV = min(minV, dist)
    print(minV)