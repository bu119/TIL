from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().split())))))

for i in combinations_with_replacement(arr, m):
    print(' '.join(i))