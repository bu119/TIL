import sys
sys.stdin = open("farm_input.txt", "r")

t = int(input())
for tc in range(t):
    n = int(input())
    arr = []
    for num in range(n):
        profit = list(map(int, input()))
        arr.append(profit)
# 행렬의 중심을 기준으로 위아래로 범위를 양쪽에서 줄여나가면서 더한다.
    center = n // 2
    total = sum(arr[center]) # 중간 행 따로 계산
    for i in range(1, n//2+1):  # n//2 + 1 번 시행
        total += sum(arr[center-i][i:-i]) + sum(arr[center+i][i:-i]) # 대칭하는 행을 한꺼번에 계산

    print(f'#{tc+1} {total}')

