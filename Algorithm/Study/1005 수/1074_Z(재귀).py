def zzz(x, y, size, ans):

    if not x <= r < x + size or not y <= c < y + size:
        return

    if x == r and y == c:
        print(ans)
        exit(0)
    else:
        size //= 2
        # 사분면 나누기
        zzz(x, y, size, ans)
        zzz(x, y + size, size, ans + size**2)
        zzz(x + size, y, size, ans + size**2 * 2)
        zzz(x + size, y + size, size, ans + size**2 * 3)

n, r, c = map(int, input().split())
zzz(0, 0, 2**n, 0)