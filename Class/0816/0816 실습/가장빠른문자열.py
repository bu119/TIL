import sys
sys.stdin = open("fast_input.txt", "r")

t = int(input())
for tc in range(t):
    a, b = input().split()
    an = len(a)
    bn = len(b) # 적음
    cnt = 0
    result = 1
    while result:
        result = 0
        for i in range(len(a)):
            if a[i:i+bn] == b:
                cnt += 1
                a = a[:i] + '-' + a[i+bn:]  # ssaa sa 경우 때문에 넣어줌
                result = 1
                break

    min_cnt = an - cnt*(bn-1)
    print(f'#{tc + 1} {min_cnt}')  # a의 길이에서 (중복되는 단어 길이-1) 만큼 빼줌