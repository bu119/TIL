import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
    arr += list(map(int, input().split()))
    arr.sort()
    arr = arr[n:]

print(arr[0])




