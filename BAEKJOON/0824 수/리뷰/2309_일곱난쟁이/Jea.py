import sys
from itertools import combinations

N = []
for i in range(9):
    N += [int(sys.stdin.readline())]
# 키로 이루어진 리스트를 만듬
# combinations이 조합을 구하는 함수 (리스트에 있는 값들의 모든 조합)
# N명 중에 7을 뽑은 경우의 수를 list에 넣음
temp = list(combinations(N, 7))
for dwarf in temp:
    if sum(dwarf) == 100:   # 합이 100인 리스트를 찾아
        dwarf = sorted(list(dwarf))  # 오름차순으로 정렬하고
        print(*dwarf, sep='\n')      # 프린트
        break