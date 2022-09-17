import sys
sys.stdin = open('testcase/input_사칙.txt')

def postorder(k):
    if num[k] != 0:
        return num[k]
    else:
        a = postorder(ch1[k])
        b = postorder(ch2[k])
        o = oper[k]
        if o == '+':
            return a + b
        elif o == '-':
            return a - b
        elif o == '*':
            return a * b
        elif o == '/':
            return a // b

for tc in range(10):
    n = int(input())
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    oper = [0] * (n + 1)
    num = [0] * (n + 1)
    for i in range(n):
        idx, *tmp = input().split()
        idx = int(idx)
        if tmp[0].isdigit():
            num[idx] = int(tmp[0])
        else:
            oper[idx] = tmp[0]
            ch1[idx] = int(tmp[1])
            ch2[idx] = int(tmp[2])
    # print(ch1)
    # print(ch2)
    # print(num)
    # print(oper)
    print(f'#{tc+1} {postorder(1)}')
