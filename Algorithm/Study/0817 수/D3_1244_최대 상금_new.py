import sys
sys.stdin = open("max_input.txt", "r")

t = int(input())
for tc in range(t):
    array, num = input().split()
    num = int(num)
    arr = list(map(int, array))

    n = len(arr)
    repeat = 0
    i = 0
    if arr == sorted(arr, reverse=True):
        for i in range(num):
            arr[-1], arr[-2] = arr[-2], arr[-1]
    else:
        while repeat < num:
            if i < len(arr):   # arr의 길이만큼 반복
                maxidx = i
                for j in range(n - 1, i, -1):
                    if arr[maxidx] < arr[j]:  # 최대값 인덱스 찾기
                        maxidx = j
                arr[i], arr[maxidx] = arr[maxidx], arr[i]
            else:   # arr의 길이를 벗어나면 뒤에 두자리만 반복
                arr[-1], arr[-2] = arr[-2], arr[-1]

            if maxidx != i + 1:
                repeat += 1
            i += 1

        if 1 < num <= n//2:
            for k in range(num-1):
                if arr[k] == arr[k + 1]:
                    a = n - 1 - k
                    b = n - 2 - k
                    if arr[a] > arr[b]:
                        arr[a], arr[b] = arr[b], arr[a]
        else:
            for k in range(n//2-1):
                if arr[k] == arr[k + 1]:
                    a = n - 1 - k
                    b = n - 2 - k
                    if arr[a] > arr[b]:
                        arr[a], arr[b] = arr[b], arr[a]
    money = ''.join(map(str, arr))
    print(f'#{tc+1} {money}')


