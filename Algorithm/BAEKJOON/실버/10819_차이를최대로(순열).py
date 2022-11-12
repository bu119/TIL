from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

per = list(permutations(a, n))
ans = 0

for arr in per:
    result = 0
    for i in range(n-1):
        result += abs(arr[i] - arr[i+1])
    if ans < result:
        ans = result
print(ans)