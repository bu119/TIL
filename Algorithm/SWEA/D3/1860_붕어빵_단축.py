import sys
sys.stdin = open('testcase/붕어빵_mine.txt')

t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())   # n명, m초에 k개 붕어빵 만듬
    sec = list(map(int, input().split()))       # 각각 도착시간

    sec.sort()
    lag = sec[-1] // m
    arr = [0] * (lag + 1)    # 붕어빵 저장
    flag = 1
    for i in range(1, lag+1):
        arr[i] = k

    cnt = sum(arr[:sec[0]//m + 1])

    for j in range(n):
        if j > 0:
            cnt += sum(arr[sec[j-1]//m + 1: sec[j]//m + 1])
        if cnt > 0:
            cnt -= 1
        else:
            flag = 0
            break

    if flag:
        print(f'#{tc+1} Possible')
    else:
        print(f'#{tc+1} Impossible')


