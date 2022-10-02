n, k = map(int, input().split())
temp = list(map(int, input().split()))
ans = 0
for i in range(n-k+1):
    total = 0
    for j in range(k):
        total += temp[i+j]
        if ans < total:
            ans = total
print(ans)