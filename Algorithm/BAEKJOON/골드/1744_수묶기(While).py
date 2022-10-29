n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
ans = idx = 0

while idx < n:
    if idx+1 < n and arr[idx] < 1 and arr[idx+1] < 1:               # 0 포함 음수가 짝수개
        ans += arr[idx] * arr[idx+1]
        idx += 2
    elif (n - idx) % 2 == 0 and arr[idx] > 1 and arr[idx+1] > 1:    # 1보다 큰 양수가 짝수개 남을 때
        ans += arr[idx] * arr[idx + 1]
        idx += 2
    else:
        ans += arr[idx]
        idx += 1

print(ans)