import sys
sys.stdin = open('testcase/퍼펙트셔플_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = input().split()
    mix = [0] * n
    num = n//2
    if n % 2 == 0:
        for i in range(num):
            mix[i * 2] = arr[i]
            mix[i * 2 + 1] = arr[ i + num ]
    else:
        for i in range(num+1):
            mix[i * 2] = arr[i]
            if i * 2 < n-2:
                mix[i * 2 + 1] = arr[ i + num + 1 ]
    mix_str = ' '.join(mix)
    print(f'#{tc+1} {mix_str}')