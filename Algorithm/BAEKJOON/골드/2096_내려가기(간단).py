import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
minV = arr
maxV = arr

for _ in range(n-1):
    arr = list(map(int, input().split()))
    minV = [min(minV[0], minV[1]) + arr[0], min(minV[0], minV[1], minV[2]) + arr[1], min(minV[1], minV[2]) + arr[2]]
    maxV = [max(maxV[0], maxV[1]) + arr[0], max(maxV[0], maxV[1], maxV[2]) + arr[1], max(maxV[1], maxV[2]) + arr[2]]

print(max(maxV), min(minV))