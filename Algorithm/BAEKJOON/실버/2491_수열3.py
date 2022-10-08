n = int(input())
arr = list(map(int, input().split()))
big = small = ans = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        big += 1
        small += 1
    elif arr[i] < arr[i+1]:
        big += 1
        if ans < small:
            ans = small
        small = 1
    else:
        small += 1
        if ans < big:
            ans = big
        big = 1
ans = max(ans, big, small)
print(ans)