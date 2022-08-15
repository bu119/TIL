import sys
sys.stdin = open("s_input.txt", "r")

for t in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    cycle = 0 # 빼는수

    while 0 not in arr:
        cycle = (cycle % 5) + 1  # 빼는 수는 1-5까지 반복 (5로 나눈 나머지 +1)

        change = arr[0] - cycle # 처음 수에서 cycle을 뺀다.
        arr.append(change)      # 계산 된 수를 마지막에 추가해준다.
        arr = arr[1:]           # 처음 수를 제외한리스트를 담는다.

        if arr[7] < 0:
            arr[7] = 0
            break

    password = ' '.join(map(str, arr))
    print(f'#{tc} {password}')

# 같은 인덱스에 대해 반복 수행하므로 i에 대해 정의 할 필요없다.
