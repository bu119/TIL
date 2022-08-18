def brute_force(p, t):
    for i in range(N - M + 1):
        flag = 1  # 참이라고 가정
        for j in range(M):
            if t[i + j] != p[j]:  # 인덱스 조절
                flag = 0
                break
        if flag:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    text = input()
    N = len(text)
    M = len(pattern)

    print(f'#{tc} {brute_force(pattern, text)}')

