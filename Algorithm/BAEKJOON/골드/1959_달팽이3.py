m, n = map(int, input().split())  # m * n

if m > n:
    print(n*2-1)

else:
    print(m*2-2)


if m == n:
    if m % 2:
        print(m // 2 + 1, n // 2 + 1)
    else:
        print(m // 2 + 1, n // 2)

elif m > n:
    if n % 2:
        print(n//2+1+(m-n) // 2, n // 2 + 1)
    else:
        print(n//2+1, n//2)
else:
    if m % 2:
        print(m // 2 + 1, m//2+1+(n-m))
    else:
        print(m //2+1, m // 2)
