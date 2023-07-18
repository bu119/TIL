t = int(input())
for tc in range(t):
    n, m, q = map(int, input().split())
    mold = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    row_max = [max(row) for row in mold]  # 각 행의 최대값 계산
    col_max = [max(col) for col in zip(*mold)]  # 각 열의 최대값 계산

    for _ in range(q):
        r, c, x = map(int, input().split())
        mold[r - 1][c - 1] = x
        row_max[r - 1] = max(row_max[r - 1], x)  # 행의 최대값 업데이트
        col_max[c - 1] = max(col_max[c - 1], x)  # 열의 최대값 업데이트

        for i in range(n):
            for j in range(m):
                if mold[i][j] == row_max[i] and mold[i][j] == col_max[j]:
                    ans += 1

    print(f'#{tc + 1} {ans}')
