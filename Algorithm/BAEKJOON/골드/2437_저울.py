import sys
input = sys.stdin.readline

n = int(input())
weights = sorted(map(int,input().split()))
print(weights)
# 누적합
ssum = 0
for weight in weights:
    if ssum + 1 < weight:
        break
    ssum += weight

print(ssum + 1)