n, k = map(int, input().split())
temp = list(map(int, input().split()))

ans = total = sum(temp[:k])

for i in range(n-k):
    total = total - temp[i] + temp[i+k]
    if ans < total:
        ans = total

print(ans)