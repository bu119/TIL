def perm(n, k, ssum):
    global ans
    if ans < ssum: return

    if n == k:
        if ans > ssum: ans = ssum
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k + 1, ssum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]


T = int(input())
for tc in range(1, T + 1):
    ans = 987654321
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = list(range(N))
    perm(N, 0, 0)
    print(f'#{tc} {ans}')