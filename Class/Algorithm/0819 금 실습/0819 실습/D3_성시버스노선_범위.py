import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(t):
    n = int(input()) # n개 노선
    busstop = [list(map(int, input().split())) for _ in range(n)]
    p = int(input()) # p개 버스정류장
    c = [int(input()) for _ in range(p)] # 각 정류장을 지나는 노선 개수
    print(f'#{tc+1}', end=' ')

    for i in range(p):
        cnt = 0
        for j in range(n):
            if c[i] >= busstop[j][0] and c[i] <= busstop[j][1]:
                cnt += 1
        print(cnt, end=' ')
    print()





