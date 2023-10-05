from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = list(map(str, range(1,n+1)))

for data in combinations_with_replacement(arr, m):
    print(' '.join(data))