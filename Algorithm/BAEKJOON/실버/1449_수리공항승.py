n, l = map(int, input().split())
leak = list(map(int,input().split()))
leak.sort()
cnt = 1
start = 0
for i in range(1, n):
    if leak[start] - 0.5 + l < leak[i]:
        start = i
        cnt += 1
print(cnt)