from itertools import permutations

n, m = map(int, input().split())
arr = map(int, input().split())
ans = sorted(set(permutations(arr, m)))

for i in ans:
    print(*i)