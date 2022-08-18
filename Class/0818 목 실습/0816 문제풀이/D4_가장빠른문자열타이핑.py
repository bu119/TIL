T = int(input())
for tc in range(1, T+1):
    text, pattern = map(str, input().split())
    N = len(text)
    M = len(pattern)

    cnt = 0
    i = 0
    while i < N-M+1:
        flag = 1
        for j in range(M):
            if text[i+j] != pattern[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i = i + M - 1   # i가 패턴길이만큼 이동
        i += 1

    print(f'#{tc} {N - M * cnt + cnt}')