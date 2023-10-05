import sys
input = sys.stdin.readline

def operation(a, b):
    cnt = 0

    while b > a:
        if b % 10 == 1:
            b = (b-1) // 10
        elif b % 2 == 0:
            b //= 2
        else:
            return -1

        cnt += 1

    if a == b:
        return cnt + 1
    return -1


A, B = map(int, input().split())
print(operation(A, B))