import sys
input = sys.stdin.readline

n = int(input())

minV = [0]*3
minT = [0]*3
maxV = [0]*3
maxT = [0]*3

for _ in range(n):
    arr = list(map(int, input().split()))

    minT[0] = min(minV[0], minV[1]) + arr[0]
    minT[1] = min(minV[0], minV[1], minV[2]) + arr[1]
    minT[2] = min(minV[1], minV[2]) + arr[2]

    maxT[0] = max(maxV[0], maxV[1]) + arr[0]
    maxT[1] = max(maxV[0], maxV[1], maxV[2]) + arr[1]
    maxT[2] = max(maxV[1], maxV[2]) + arr[2]

    for i in range(3):
        minV[i] = minT[i]
        maxV[i] = maxT[i]

print(max(maxV), min(minV))