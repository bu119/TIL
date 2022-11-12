n = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = []
b = []
ansA = ansB = 0

m = n//2

if n % 2:                       # 홀수개
    for i in range(m):
        a += [arr[i], arr[m + 1 + i]]
        b += [arr[m + 1 + i], arr[i]]
    a += [arr[m]]
    b += [arr[m]]


else:                           # 짝수개
    for i in range(m):
        a += [arr[i], arr[m + i]]
        b += [arr[m + i], arr[i]]

for j in range(n-1):
    ansA += abs(a[j] - a[j+1])
    ansB += abs(b[j] - b[j + 1])

print(max(ansA, ansB))
