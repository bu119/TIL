from itertools import combinations

while True:
    k, *arr = map(int, input().split())

    if k == 0:
        break

    for lotto in combinations(arr, 6):
        print(*lotto)
    print()