n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    ssum = 0
    for j in range(i, n):
        ssum += arr[j]
        if ssum == s:
            cnt += 1
print(cnt)

