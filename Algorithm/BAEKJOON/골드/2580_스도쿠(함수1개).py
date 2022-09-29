def dfs(k):
    global flag
    global sudoku

    if flag:
        return

    if k == len(zero):
        flag = 1
        for p in sudoku:
            print(' '.join(map(str, p)))
        return

    else:
        i = zero[k][0]
        j = zero[k][1]
        num = []

        # 가로
        for x in range(1, 10):
            if x not in sudoku[i]:
                num.append(x)
        # 세로
        for y in range(9):
            tmp = sudoku[y][j]
            if tmp in num:
                num.remove(tmp)

        # 사각형
        a = i // 3
        b = j // 3
        for r in range(3):
            for c in range(3):
                tmp = sudoku[a * 3 + r][b * 3 + c]
                if tmp in num:
                    num.remove(tmp)

        for n in num:
            sudoku[i][j] = n
            dfs(k+1)
            sudoku[i][j] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i, j))

flag = 0
dfs(0)