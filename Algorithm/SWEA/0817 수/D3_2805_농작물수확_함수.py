import sys
sys.stdin = open("farm_input.txt", "r")

def add(arr): # sum함수 대신 사용
    sum_arr = 0
    for i in arr:
        sum_arr += i
    return sum_arr

t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for num in range(n):
        profit = list(map(int, input()))
        arr.append(profit)
# 행렬의 중심을 기준으로 위아래로 범위를 양쪽에서 줄여나가면서 더한다.
    center = n // 2
    total = add(arr[center])
    for i in range(n//2+1):  # n//2 + 1 번 시행
        total += add(arr[center-i][i:-i]) + add(arr[center+i][i:-i]) # 대칭하는 행을 한꺼번에 계산
    print(f'#{tc+1} {total}')
