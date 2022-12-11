import sys
input = sys.stdin.readline

# 완전 탐색
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = n
for i in range(n-1):
    ssum = 0
    for j in range(i, n):
        ssum += arr[j]
        if ssum >= s:
            if j-i+1 < cnt:
                cnt = j-i+1
            break
print(cnt)
