import sys
sys.stdin = open("어디_input.txt", "r")

def count_puzzle(arr):
    cnt = 0
    for row in range(n):
        sum_row = 0
        for col in range(n):
            sum_row += arr[row][col] # 자리수를 차례대로 더함

            if arr[row][col] == 0:   # 0을 만나면
                if sum_row == k:     # k 만큼 자리 수가 있는 지 확인하고
                    cnt += 1         # 있으면 카운트
                sum_row = 0          # sum 초기화

        if sum_row == k:             # 행의 끝에 0 안 만났을 때 sum이 k이면
            cnt += 1                 # 카운트 한다.
    return cnt

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_row = count_puzzle(arr)
    arr = list(zip(*arr))
    arr_col = count_puzzle(arr)

    print(f'#{tc+1} {arr_row + arr_col}')