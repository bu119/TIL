import sys
sys.stdin = open('testcase/퍼펙트셔플_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = input().split()
    div = n//2 + n % 2     # 자르는 경계: 홀수면 + 1
    arr_l = arr[:div]
    arr_r = arr[div:]
    mix = []
    for i in range(div):
        mix.append(arr_l[i])
        if i < n - div:   # arr_r 길이 보다 작을 때
            mix.append(arr_r[i])

    mix_str = ' '.join(mix)
    print(f'#{tc + 1} {mix_str}')