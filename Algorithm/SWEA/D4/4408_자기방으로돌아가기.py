import sys
sys.stdin = open('testcase/방_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    hall = [0] * 201  # 복도를 기준으로 칸 만들기
    for i in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        start = (s+1)//2
        end = (e+1)//2
        for j in range(start, end+1):
            hall[j] += 1

    print(f'#{tc+1} {max(hall)}')