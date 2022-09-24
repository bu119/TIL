import sys
sys.stdin = open('testcase/input_베비진.txt')

def result(arr, i):
    if i % 2 == 0:
        p = 1
    else:
        p = 2

    if 3 in arr:
        return p
    else:
        for k in range(8):
            if arr[k] and arr[k+1] and arr[k+2]:
                return p
    return 0

t = int(input())
for tc in range(t):
    num = list(map(int, input().split()))
    first = [0] * 10
    second = [0] * 10
    ans = 0
    for i in range(12):
        if i % 2 == 0:                           # 플레이어 1
            first[num[i]] += 1
            if i >= 4:
                ans = result(first, i)
        else:                                    # 플레이어 2
            second[num[i]] += 1
            if i >= 5:
                ans = result(second, i)
        if ans:
            break
    # print(first)
    # print(second)
    print(f'#{tc+1} {ans}')
