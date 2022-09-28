n = int(input())
num = list(map(int, input().split()))

m = max(num)
total = 0
for i in range(n):
    total += num[i] / m * 100

print(total / n)