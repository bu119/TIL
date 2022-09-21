def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # 정점수, 시작정점
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    temp = list(map(int, input().split()))

    for i in range(E):
        p = temp[i * 2]
        c = temp[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')