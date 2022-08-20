import sys
sys.stdin = open("s_input.txt", "r")

t = int(input())
for tc in range(t):
    n = int(input()) # n개 노선
    busstop = []
    for num in range(n):
        a, b = map(int, input().split()) # a<= 정류장 번호 <=b
        busstop += range(a, b+1)
    p = int(input()) # p개 버스정류장
    c = [int(input()) for _ in range(p)] # 각 정류장을 지나는 노선 개수
    print(f'#{tc+1}', end=' ')

    for i in c:
        cnt = 0
        for j in busstop:
            if i == j:
                cnt += 1
        print(cnt, end=' ')
    print()





