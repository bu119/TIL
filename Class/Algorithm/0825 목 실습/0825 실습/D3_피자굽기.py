import sys
sys.stdin = open('testcase/피자_input.txt')

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    ci = list(map(int, input().split()))
    arr = ci[:n]             # 화덕크기에 맞는 배열
    idx = list(range(n))     # 변화하는 인덱스 저장
    idx_m = n-1              # 인덱스
    stop = 1
    while stop:
        for i in range(n):
            arr[i] = arr[i] // 2
            if arr[i] == 0:
                if idx_m < m-1:     # 화덕에 들어갈 피자가 남아있음
                    idx_m += 1
                    arr[i] = ci[idx_m]
                    idx[i] = idx_m
                else:               # 화덕에 피자가 다들어감
                    idx[i] = 0
            if idx.count(0) == n-1: # 피자 1개 남으면 멈춤
                stop = 0
                break
    for j in idx:
        if j != 0:
            print(f'#{tc+1} {j+1}')
            break





