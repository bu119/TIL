n = int(input())
arr = [0] * (n+1)
for i in range(2, n+1):
    arr[i] = arr[i-1] + 1   # -1이 있으므로 바로 전 단계에서 +1을 한 경우의 수
    if i % 6 == 0:          # 2와 3 먼저 나누는 수에 따라 경우의 수가 바뀜
        arr[i] = min(arr[i // 3] + 1, arr[i // 2] + 1, arr[i])
    elif i % 3 == 0:
        arr[i] = min(arr[i//3] + 1, arr[i])   # 바로 전 단계의 경우의 수와 나누기를 하고 난 뒤 나온 수의 경우의 수를 비교 해야한다.
    elif i % 2 == 0:
        arr[i] = min(arr[i//2] + 1, arr[i])


print(arr[n])