import sys; sys.stdin = open('삼성시의버스노선_input.txt')

T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 5001
    N = int(input())

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            cnt[j] += 1

    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P):
        temp = int(input())
        print(f'{cnt[temp]}', end=' ')
    print()