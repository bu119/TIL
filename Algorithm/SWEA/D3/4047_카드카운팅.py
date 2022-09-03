import sys
sys.stdin = open('testcase/카드_input.txt')

t = int(input())
for tc in range(t):
    s = input()
    cnt = {'S':13, 'D':13, 'H':13, 'C':13}
    flag = 0
    for i in range(0, len(s), 3):
        if s[i:i+3] in s[i+3:]:
            flag = 1
            break
        else:
            cnt[s[i]] -= 1

    print(f'#{tc+1}', end=' ')
    if flag:
        print('ERROR')
    else:
        print(cnt['S'], cnt['D'], cnt['H'], cnt['C'])
