n = int(input())
arr = list(map(int, input().split()))
big = small = ans = 1

for i in range(1, n):
    if arr[i-1] == arr[i]:
        big += 1
        small += 1
    elif arr[i-1] < arr[i]:
        big += 1
        ans = max(ans, small)
        small = 1
    else:
        small += 1
        ans = max(ans, big)
        big = 1
ans = max(ans, big, small)

print(ans)