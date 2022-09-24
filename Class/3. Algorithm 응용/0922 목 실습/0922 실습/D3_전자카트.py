import sys
sys.stdin = (open('testcase/input_전자카트.txt'))

def perm(n, k, ssum):
    global ans

    if ssum > ans:
        return

    if n == k:
        ssum += arr[p[-2] - 1][p[k] - 1]
        if ans > ssum:
            ans = ssum
    else:
        for i in range(n):
            if not visited[i]:
                p[k] = num[i]
                visited[i] = 1
                perm(n, k + 1, ssum + arr[p[k - 1] - 1][p[k] - 1])
                visited[i] = 0


t = int(input())
for tc in range(t):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = list(range(1, N + 1))
    p = [0] * (N + 1)
    p[0] = p[N] = num[0]
    visited = [0] * N
    visited[0] = 1

    ans = 10000
    perm(N, 1, 0)
    print(f'#{tc+1} {ans}')