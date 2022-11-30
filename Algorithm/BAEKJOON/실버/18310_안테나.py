import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = arr[-1] * n
for i in range(n//2 - 1, n//2 + 1):
    ssum = 0
    for j in range(n):
        ssum += abs(arr[i] - arr[j])

    if ssum < ans:
        ans = ssum
        num = arr[i]

print(num)
