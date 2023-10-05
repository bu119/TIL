import sys
input = sys.stdin.readline

n = int(input())
graph = [0]*1001
maxV = [0, 0]
for _ in range(n):
    l, h = map(int, input().split())
    graph[l] = h
    if maxV[1] < h:
        maxV[0] = l
        maxV[1] = h

area = 0
# 왼쪽
maxL = 0
for i in range(maxV[0]):
    if graph[i] and maxL == 0:
        maxL = graph[i]

    elif maxL < graph[i]:
        maxL = graph[i]

    area += maxL
# 오른쪽
maxR = 0
for j in range(1000, maxV[0]-1, -1):
    if graph[j] and maxR == 0:
        maxR = graph[j]

    elif maxR < graph[j]:
        maxR = graph[j]

    area += maxR

print(area)