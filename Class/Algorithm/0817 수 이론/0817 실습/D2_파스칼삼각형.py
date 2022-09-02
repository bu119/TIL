import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [[0]*10 for i in range(10)]

    print(f'#{tc+1}')

    for i in range(10):
        for j in range(10):
            if j == 0:
                arr[i][j] = 1
            if i == j:
                arr[i][j] = 1

    for r in range(2,10):
        for c in range(1,9):
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]

    for k in range(n):
        pascal = ' '.join(map(str, arr[k][:k+1]))
        print(pascal)
