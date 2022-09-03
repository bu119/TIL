import sys
sys.stdin = open("ns_input.txt", "r")

for tc in range(10):
    n = int(input())
    arr = []
    for num in range(100):
        ns = list(map(int, input().split()))
        arr.append(ns)

# N극이 위, S극이 아래에 있으므로
# 자성체의 위치는 1(N극 성질)이 먼저 다음 2(S극 성질)가 와야 교착 상태가 된다.
# 1이 먼저 오고 다음 2가 오면서 합이 3이 되면 교착 상태 개수 추가
    cnt = 0
    for i in range(100):
        sum_ns = 0
        for j in range(100):
            if arr[j][i] == 1: # 각 열끼리 비교해야 하므로 열은 고정하고 행을 변화시킴
                sum_ns = 0     # 값이 1 이면 sum_ns 초기화

            sum_ns += arr[j][i] # 요소의 값을 계속 더 한다.

            if sum_ns == 3: # 합이 3이되면 교착상태 추가
                cnt += 1
                sum_ns = 0
    print(f'#{tc+1} {cnt}')



