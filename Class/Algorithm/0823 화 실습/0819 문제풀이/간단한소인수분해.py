import sys; sys.stdin = open('간단한소인수분해_input.txt')

T = int(input())
for tc in range(1, T+1):
    number = int(input())
    prime = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(prime)):
        while number % prime[i] == 0:
            cnt[i] += 1
            number //= prime[i]

    print(f'#{tc} {" ".join(map(str, cnt))}')
