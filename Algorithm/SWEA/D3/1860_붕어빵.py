import sys
sys.stdin = open('testcase/붕어빵_input.txt')

t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())   # n명, m초에 k개 붕어빵 만듬
    sec = list(map(int, input().split()))       # 각각 도착 시간
    #  기다리는 시간이 없으면 “Possible”, 아니면 “Impossible”

    sec.sort()
    lag = sec[-1]
    arr = [0] * (lag + 1)    # 붕어빵 저장
    flag = 1
    for i in range(m, lag+1, m):     # 각 시간에 만들어 진 붕어빵 개수 저장
        arr[i] = k
    cnt = sum(arr[:sec[0] + 1])      # 첫 사람이 올 때 붕어빵 개수

    for j in range(n):
        if j > 0:              # 두번째 부터 사람이 올 때 까지 붕어빵을 만든 개수를 저장
            cnt += sum(arr[sec[j-1] + 1: sec[j] + 1])
        if cnt > 0:            # 빵이 있으면 빵-1
            cnt -= 1
        else:                  # 빵이 없으면 break
            flag = 0
            break

    if flag:
        print(f'#{tc+1} Possible')
    else:
        print(f'#{tc+1} Impossible')


