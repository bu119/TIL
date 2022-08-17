import sys
sys.stdin = open("fast_input.txt", "r")

t = int(input())
for tc in range(t):
    a, b = input().split()
    an = len(a)
    bn = len(b) # 적음
    cnt = 0
    # for i in range(an-bn+1):
    #     if a[i:i+bn] == b:
    #         cnt += 1
    # min_cnt = an - cnt*(bn-1)

    s_idx = []
    for i in range(an-bn+1):
        if b[0] == a[i]:
            s_idx.append(i)
    result = 0
    for j in s_idx: # a에서 b의 첫번째 문자가 있는 인덱스 모음
        cnt = 0
        for k in b: # b문자
            if k in a[j:]:
                cnt += 1
        if cnt == bn:
            result += 1

    min_cnt = an - result * (bn - 1)
    print(f'#{tc + 1} {min_cnt}')  # a의 길이에서 (중복되는 단어 길이-1) 만큼 빼줌