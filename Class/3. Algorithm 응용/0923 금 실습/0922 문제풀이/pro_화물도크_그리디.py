T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    # 종료시간 순으로 정렬
    jobs.sort(key=lambda x:(x[1], x[0]))
    ans = 0
    finish = 0
    for i in range(N):
        if finish <= jobs[i][0]:
            ans += 1
            finish = jobs[i][1]
    print(f'#{tc} {ans}')