n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ansA = ansB = 0

a = arr[:n//2]
if n % 2:                       # 홀수
    b = arr[n//2+1:]
    m = arr[n//2]
else:                           # 짝수
    b = arr[n//2:]

for i in range(n//2):
    ansA += abs(a[i] - b[i])    # a 먼저
    ansB += abs(b[i] - a[i])    # b 먼저
    if i+1 < n//2:
        ansA += abs(a[i+1] - b[i])
        ansB += abs(b[i+1] - a[i])

if n % 2:                       # 홀수
    ansA += abs(b[-1] - m)
    ansB += abs(a[-1] - m)

print(max(ansA, ansB))