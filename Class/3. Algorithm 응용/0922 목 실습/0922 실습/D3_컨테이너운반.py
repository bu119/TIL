import sys
sys.stdin = open('testcase/input_컨테이너.txt')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())        # n 컨테이너, m 트럭
    w = list(map(int, input().split()))     # 컨테이너 무게
    t = list(map(int, input().split()))     # 트럭 용량

    w.sort(reverse=True)
    t.sort(reverse=True)

    total = 0
    for i in range(m):
        for j in range(len(w)):
            if t[i] >= w[j]:
                total += w.pop(j)
                break
    print(f'#{tc+1} {total}')


