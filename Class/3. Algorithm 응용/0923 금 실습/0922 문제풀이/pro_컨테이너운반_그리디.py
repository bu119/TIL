T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 컨테이너, 트럭
    W = list(map(int, input().split()))  # 화물
    T = list(map(int, input().split()))  # 트럭

    W.sort(reverse=True)
    T.sort(reverse=True)

    i = j = ans = 0
    while i < N and j < M:
        if W[i] <= T[j]:
            ans += W[i]
            i, j = i + 1, j + 1
        else:
            i += 1
    print(f'#{tc} {ans}')