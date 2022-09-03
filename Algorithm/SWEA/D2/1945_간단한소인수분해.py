# 1945.간단한 소인수분해
t = int(input())
for tc in range(t):
    num = int(input())

    def involution(num, n):
        cnt = 0
        while num % n == 0:
            num = num // n
            cnt += 1
        return cnt

    print(f'#{tc+1} {involution(num, 2)} {involution(num, 3)} {involution(num, 5)} {involution(num, 7)} {involution(num, 11)}')
