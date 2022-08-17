t = int(input())
for tc in range(t):
    n, case = map(int, input().split())
    print(f'#{tc + 1}')

    if case == 1:
        for i in range(n):
            print('*' * (i+1))
    elif case == 2:
        for i in range(n-1, -1, -1):
            print('*' * (i+1))
    elif case == 3:
        for i in range(n):
            print(' ' * (n-1 - i) + '*' * (2 * i + 1))


