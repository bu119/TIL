import sys
sys.stdin = open('testcase/농작물_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    total = sum(farm[n//2])         # 중간 행
    for i in range(1, n//2 + 1):
        total += sum(farm[n//2 - i][i:n-i]) + sum(farm[n//2 + i][i:n-i])
        # 중간 행 위, 아래 인덱스 줄여가면서 더하기
    print(f'#{tc+1} {total}')