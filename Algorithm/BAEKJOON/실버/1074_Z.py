n, r, c = map(int, input().split())

# 4분면을 나눠서 나눈 사분면에서 또 사분면을 나눠서 탐색

ans = 0
while n > 0:
    n -= 1

    # 1사분면
    if r < 2**n and c >= 2**n:
        ans += 2 ** (2*n)
        c -= 2 ** n

    # 2사분면
    elif r < 2**n and c < 2**n:
        ans += 0

    # 3사분면
    elif r >= 2**n and c < 2**n:
        ans += 2 ** (2*n) * 2
        r -= 2 ** n

    # 4사분면
    else:
        ans += 2 ** (2*n) * 3
        r -= 2 ** n
        c -= 2 ** n
    # print(n, r, c, ans)

print(ans)