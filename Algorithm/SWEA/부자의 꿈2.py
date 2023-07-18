t = int(input())
for tc in range(t):
    n, m, q = map(int, input().split())
    mold = []
    row_max = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mold.append(row)
        # 각 행의 최대값 계산
        row_max.append(max(row))

    ans = 0
    col_max = [max(col) for col in zip(*mold)]  # 각 열의 최대값 계산

    row_set = set(row_max)
    col_set = set(col_max)

    for _ in range(q):
        r, c, x = map(int, input().split())
        mold[r - 1][c - 1] = x

        if row_max[r - 1] < x:
            row_set.remove(row_max[r - 1])
            row_max[r - 1] = x
            row_set.add(x)

        if col_max[c - 1] < x:
            col_set.remove(col_max[c - 1])
            col_max[c - 1] = x
            col_set.add(x)

        # for i in range(n):
        #     for j in range(m):
        #         if mold[i][j] == row_max[i] and mold[i][j] == col_max[j]:
        #             ans += 1

        ans += len(row_set & col_set)

    print(f'#{tc + 1} {ans}')
