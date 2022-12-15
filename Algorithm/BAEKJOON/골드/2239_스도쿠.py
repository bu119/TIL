def check(r, c, x):
    # 같은 값이 있는지 확인 - 있으면 0, 없으면 1

    # 가로
    if x in sudoku[r]:
        return 0

    # 세로
    for y in range(9):
        if sudoku[y][c] == x:
            return 0

    # 3*3 square
    square_r = (r//3) * 3
    square_c = (c//3) * 3
    for ir in range(square_r, square_r+3):
        for jc in range(square_c, square_c+3):
            if sudoku[ir][jc] == x:
                return 0
    return 1


def dfs(k):

    if k == len(empty):
        for z in sudoku:
            print(''.join(map(str, z)))
        exit(0)

    r, c = empty[k]
    for x in range(1, 10):
        if check(r, c, x):
            sudoku[r][c] = x
            dfs(k+1)
            sudoku[r][c] = 0


sudoku = [list(map(int, input())) for _ in range(9)]
empty = []
# print(sudoku)

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append((i, j))

dfs(0)