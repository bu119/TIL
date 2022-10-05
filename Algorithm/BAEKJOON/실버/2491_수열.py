n = int(input())
arr = list(map(int, input().split()))
big = small = 1
ans = 0
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        big += 1
        if ans < small:
            ans = small
        small = 0
    elif arr[i-1] >= arr[i]:
        small += 1
        if ans < big:
            ans = big
        big = 0
    print(small, big)


print(ans)