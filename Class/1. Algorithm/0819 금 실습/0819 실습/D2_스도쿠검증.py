import sys
sys.stdin = open("스도쿠_input.txt", "r")

t = int(input())
for tc in range(t):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for i in range(9): # 행 탐색
        for j in range(1, 10):
            if j not in arr[i]:
                result = 0

    arr_squ = []
    for si in range(0, 9, 3): # 네모 탐색
        for sj in range(0, 9, 3):
            arr_squ = arr[si][sj:sj+3]+arr[si+1][sj:sj+3]+arr[si+2][sj:sj+3]
            for k in range(1, 10):
                if k not in arr_squ:
                    result = 0

    arr_col = list(zip(*arr))
    for ci in range(9):  # 열 탐색
        for cj in range(1, 10):
            if cj not in arr_col[ci]:
                result = 0

    print(f'#{tc+1} {result}')