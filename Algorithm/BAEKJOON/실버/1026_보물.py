n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()),reverse=True)

ssum = 0
for i in range(n):
    ssum += a[i]*b[i]
print(ssum)