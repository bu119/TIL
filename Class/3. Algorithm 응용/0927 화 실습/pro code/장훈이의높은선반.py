import sys; sys.stdin = open('장훈이의높은선반_input.txt')

def powerset(n, k, ssum):
    global ans
    if ans < ssum: return

    if n == k:
        if ssum >= B and ans > ssum:
            ans = ssum
    else:
        b[k] = 1
        powerset(n, k+1, ssum + H[k])
        b[k] = 0
        powerset(n, k+1, ssum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # 점원수, 선반높이
    H = list(map(int, input().split()))  # 점원들의 키

    ans = 987654321
    b = [0] * N
    powerset(N, 0, 0)
    print(f'#{tc} {ans - B}')