n, k = map(int, input().split())
temp = list(map(int, input().split()))

ans = sum(temp[:k])

for i in range(n-k):
    total = sum(temp[i:i+k])
    if ans < total:
        ans = total

print(ans)