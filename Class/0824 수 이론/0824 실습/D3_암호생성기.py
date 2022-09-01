import sys
sys.stdin = open('input.txt')

for t in range(10):
    tc = input()
    arr = list(map(int, input().split()))
    cnt = 0
    while True:
        cycle = cnt % 5 + 1

        if arr[0] - cycle < 0:
            arr.append(0)
        else:
            arr.append(arr[0] - cycle)
            cnt += 1

        arr = arr[1:]

        if arr[-1] == 0:
            break

    ans = ' '.join(list(map(str, arr)))
    print(f'#{tc} {ans}')
