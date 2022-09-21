t = int(input())
for tc in range(t):
    n = float(input())
    ans = ''
    while n != 1 and n != 0:
        n *= 2
        if n >= 1:
            ans += '1'
            n -= 1
        else:
            ans += '0'

        if len(ans) > 12:
            ans = 'overflow'
            break
    print(f'#{tc+1} {ans}')