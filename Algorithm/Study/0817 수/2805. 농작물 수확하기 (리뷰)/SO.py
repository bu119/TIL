import sys
sys.stdin = open("input_sample.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 2차원 배열

    result = 0
    JS = N // 2 # 중간 행
    JE = N // 2 # 중간 행
    print(list(range(N)))
    for i in range(N):
        print(list(range(JS, JE + 1)))
        for j in range(JS, JE + 1):  # 중간 인덱스를 기준으로 열 범위 변화
            print(i,j)
            result += arr[i][j]

        if i < N // 2:  # 중간행 위에 행들은 내려오면서 열의 범위가 커짐
            JS -= 1
            JE += 1
        else:           # 중간행 아래 행들은 내려오면서 커졌던 열의 범위가 작아짐
            JS += 1
            JE -= 1

    print(f'#{tc} {result}')