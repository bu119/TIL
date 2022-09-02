import sys
sys.stdin = open('input.txt')


t = int(input())

for tc in range(t):
    n, p = map(int, input().split())
    arr = [n // p] * p
    result = 1
    for i in range(n % p):
        arr[i] += 1
    for j in arr:
        result *= j

    print(f'#{tc+1} {result}')



