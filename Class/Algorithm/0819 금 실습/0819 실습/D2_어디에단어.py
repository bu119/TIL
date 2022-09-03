import sys
sys.stdin = open("어디_input.txt", "r")

def count_puzzle(arr):
    cnt = 0
    for row in range(n):
        for col in range(n - k + 1):
            num = 0
            for c in range(k):
                num += arr[row][col + c]

            if num == k:
                if col == 0:
                    if arr[row][col + k] != 1:
                        cnt += 1
                elif col + k == n:
                    if arr[row][col - 1] != 1:
                        cnt += 1
                else:
                    if arr[row][col - 1] != 1 and arr[row][col + k] != 1:
                        cnt += 1
    return cnt

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr_row = count_puzzle(arr)
    arr = list(zip(*arr))
    arr_col = count_puzzle(arr)

    print(f'#{tc+1} {arr_row +arr_col}')