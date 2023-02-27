import copy

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
minV = copy.deepcopy(arr[0])
maxV = copy.deepcopy(arr[0])
for i in range(n-1, 0, -1):
    minV[0] += min(arr[i][0], arr[i][1])
    minV[1] += min(arr[i][0], arr[i][1], arr[i][2])
    minV[2] += min(arr[i][1], arr[i][2])

    maxV[0] += max(arr[i][0], arr[i][1])
    maxV[1] += max(arr[i][0], arr[i][1], arr[i][2])
    maxV[2] += max(arr[i][1], arr[i][2])

print(max(maxV), min(minV))