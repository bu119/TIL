import sys
sys.stdin = open("input_sample.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 2차원 배열
    mid = N // 2
    total = 0

    # 윗줄에서 아랫줄로 순차적으로 더하기
    # 중간행 위에 행
    for i in range(mid): #[0,1,...,mid-1]
        for j in range(mid - i, mid + i + 1): # 열이 i에 따라 범위가 늘어남
            total += arr[i][j]
    # 중간 행
    for i in range(N):
        total += arr[mid][i]

    # 중간행 아래행
    for i in range(1, mid + 1): #행 : [1,...,mid]
        for j in range(i, N - i): # i에 따라 한칸씩 범위가 줄어듬
            total += arr[mid + i][j]  #행 : [1+mid,...,mid+mid]

    print(f'#{tc} {total}')