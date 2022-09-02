import sys
sys.stdin = open('testcase/Magnetic_input.txt')

for tc in range(10):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(100):
        judge = 0               # judge 초기화 (합 계산)
        for j in range(100):
            judge += arr[j][i]  # 열 탐색
            if arr[j][i] == 1:  # n극 일때 1
                judge = 1       # judge 1로 초기화

            if judge == 3:      # 합이 3일 때
                cnt += 1        # cnt 추가
                judge = 0       # judge 초기화
    print(f'#{tc+1} {cnt}')



