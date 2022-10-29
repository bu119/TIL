n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
    print(arr[0])
    exit(0)

arr.sort()

ans = 0
idx = -1
for i in range(n):
    if arr[i] > 0:                              # 정렬 했을 때 양수가 처음 나오는 인덱스
        idx = i
        break

# 양수 일 때
if idx > -1:                                    # 양수가 있으면 idx가 -1 보다 커짐
    for j in range(n-1, idx-1, -2):
        if j - 1 > -1 and arr[j - 1] > 0:       # 양수가 짝수개 이면
            if arr[j - 1] == 1:                 # 하나라도 1이면 더함
                ans += arr[j] + arr[j - 1]
            else:
                ans += arr[j] * arr[j - 1]      # 하나라도 1이 아니면
        else:                                   # 양수가 홀수개 이면 마지막 양수는 더한다.
            ans += arr[j]
# 전부 음수 일 때
if idx == -1:
    idx = n

# 음수 일 때
for k in range(0, idx, 2):
    if k + 1 < n and arr[k + 1] < 1:        # 0 포함 음수가 짝수개 이면
        ans += arr[k] * arr[k + 1]
    else:                                   # 0 포함 음수가 홀수개 이면 마지막 음수는 더한다.
        ans += arr[k]

print(ans)