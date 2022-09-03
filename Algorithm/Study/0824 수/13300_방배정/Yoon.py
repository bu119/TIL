N, K = map(int, input().split())
arr = [[0]*7, [0]*7]
for _ in range(N):
    sex, num = map(int, input().split())
    arr[sex][num] += 1

total = 0
for i in range(2):
    for j in range(1, 7):
        total += arr[i][j]//K
        if arr[i][j] % K:
            total += 1
print(total)
