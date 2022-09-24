import sys
sys.stdin = open('testcase/input_최대상금.txt')


def perm(r, k):  # k는 깊이
    global cash_prize

    if r == k:
        tmp = int(''.join(arr))
        if tmp > cash_prize:
            cash_prize = tmp
        return

    if ''.join(arr) in memo[k]:
        return

    memo[k].append(''.join(arr))        # 메모

    for i in range(0, N - 1):
        for j in range(i + 1, N):
            arr[i], arr[j] = arr[j], arr[i]
            perm(r, k+1)
            arr[i], arr[j] = arr[j], arr[i]

t = int(input())
for tc in range(t):
    arr, R = input().split()
    arr = list(arr)
    N = len(arr)
    R = int(R)
    memo = [[] for _ in range(R)]
    cash_prize = 0
    perm(R, 0)
    print(f'#{tc+1} {cash_prize}')