n = int(input())
num = [0] * (n+1)

for i in range(1, n+1):
    num[i] = num[i-1] + 1
    find = int(i**(1/2)) + 1
    for j in range(2, find):
        num[i] = min(num[i], num[i-j**2] + 1)

print(num[n])