from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = map(str, sorted(map(int, input().split())))

for i in permutations(arr, m):
    print(' '.join(i))