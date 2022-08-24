import sys; sys.stdin = open('어디에단어_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 행방향
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:      # 1일 때
                cnt += 1
            else:                   # 0일 때
                if cnt == K:
                    ans += 1
                cnt = 0
        # 마지막 값이 1일 때 체크
        if cnt == K:
            ans += 1

    # 열방향
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:      # 1일 때
                cnt += 1
            else:                   # 0일 때
                if cnt == K:
                    ans += 1
                cnt = 0
        # 마지막 값이 1일 때 체크
        if cnt == K:
            ans += 1

    print(f'#{tc} {ans}')