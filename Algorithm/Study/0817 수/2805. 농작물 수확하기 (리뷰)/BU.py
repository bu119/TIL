import sys
sys.stdin = open("input_sample.txt", "r")

def add(arr): # sum함수 대신 사용
    sum_arr = 0
    for i in arr:
        sum_arr += i
    return sum_arr

t = int(input())
for tc in range(t):
    n = int(input()) # n * n 행렬
    arr = []
    for num in range(n):
        profit = list(map(int, input()))
        arr.append(profit)   # 2차원 배열
    print(arr)
# 행렬의 중심을 기준으로 위아래로 범위를 양쪽에서 줄여나가면서 더한다.
    total = 0
    center = n//2   # 중심의 행 인덱스
    for i in range(n//2+1):  # n//2 + 1 번 시행 (개수)
        if i == 0: # 중간 행
            total += add(arr[center]) # 중간 행 따로 계산
        else: # 중간행을 기준으로 멀어짐
            total += add(arr[center-i][i:-i]) + add(arr[center+i][i:-i]) # 안쪽에서 밖으로 대칭 행을 한꺼번에 계산
    print(f'#{tc+1} {total}')