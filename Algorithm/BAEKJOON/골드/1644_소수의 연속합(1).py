import math
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            # i로 나누어 떨어지면 소수가 아니므로 False 리턴
            return False
    return True


def get_prime_arr(n):
    prime_num = []
    for num in range(2,n+1):
        if is_prime_num(num):
            prime_num.append(num)

    return prime_num


n = int(input())
prime_num = get_prime_arr(n)
cnt = 0
start = 0
end = 0
ssum = 0

while True:
    if ssum >= n:
        ssum -= prime_num[start]
        start += 1
    elif end == len(prime_num):
        break
    else:
        ssum += prime_num[end]
        end += 1

    if ssum == n:
        cnt += 1

print(cnt)