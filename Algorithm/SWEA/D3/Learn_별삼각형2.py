t = int(input())
for tc in range(t):
    n, case = map(int, input().split())
    print(f'#{tc + 1}')

    if case == 1:
        for i in range(n):
            if i <= n//2:
                print('*' * (i+1))
            else:
                print('*' * (n-i))
    elif case == 2:
        for i in range(n):
            if i <= n // 2:
                print(' ' * (n-i-3) + '*' * (i + 1))
            else:
                print(' ' * (i-2) + '*' * (n-i))
    elif case == 3:
        for i in range(n):
            if i <= n // 2:
                print(' ' * i + '*' * (n-2*i))
            else:
                print(' ' * (n-1 - i) + '*' * (2*i-3))
    elif case == 4:
        for i in range(n):
            if i <= n // 2:
                print(' ' * i + '*' * (n//2+1 - i))
            else:
                print(' ' * (n//2) + '*' * (i+1 - n//2))