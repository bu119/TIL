import sys
sys.stdin = open("max_input.txt", "r")

def max_sort(arr, num): # arr배열, num 시행 횟수
    repeat = 0
    i = 0
    while repeat < num:
        if i < len(arr): # 길이 넘어가면
            maxidx = i
            for j in range(n-1, i, -1):
                if arr[maxidx] < arr[j]:  # 최대값 인덱스 찾기
                    maxidx = j
            arr[i], arr[maxidx] = arr[maxidx], arr[i]
        else: # arr의 길이를 벗어나면 뒤에 두자리만 반복
            if n - len(set(arr)) == 0:
                for i in range(num):
                    arr[-1], arr[-2] = arr[-2], arr[-1]
        if maxidx != i+1: # 최대값의 인덱스가
            repeat += 1
        i += 1
    return arr

def same(arr, scale):
    for k in range(scale - 1):
        if arr[k] == arr[k + 1]:
            a = n - 1 - k
            b = n - 2 - k
            if arr[a] > arr[b]:
                arr[a], arr[b] = arr[b], arr[a]
    return arr

t = int(input())
for tc in range(t):
    array, num = input().split()
    num = int(num)
    arr = list(map(int, array))
    n = len(arr)

    if arr == sorted(arr, reverse=True):
        if n - len(set(arr)) == 0:
            for i in range(num):
                arr[-1], arr[-2] = arr[-2], arr[-1]
    else:
        arr = max_sort(arr, num) # 만든 함수 사용

        if 1 < num <= n//2:
            arr = same(arr, num)  # 만든 함수 사용
        else:
            arr = same(arr, n//2)

    money = ''.join(map(str, arr))
    print(f'#{tc+1} {money}')