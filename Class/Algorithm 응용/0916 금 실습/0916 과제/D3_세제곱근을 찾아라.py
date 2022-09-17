t = int(input())
for tc in range(t):
    n = int(input())
    x = round(n ** (1 / 3), 2)
    if x % 1:
        ans = -1
    else:
        ans = int(x)
    print(f'#{tc+1} {ans}')