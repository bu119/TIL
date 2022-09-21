# 먼저 16진수를 2진수로 바꾸면서 입력받기
# 첫번째굴 위에도 0 오른쪽 0 으로 값 받기
# 맨앞에 없어도 9개 가 구분된다. (비율에서 포함안시켜도 된다.)
# 16진수를 2진수로 바꾸려면 매핑 ㅌㅔ이블 만들기 (0부터 F까지)
import sys
sys.stdin = open('input_암호코드스캔.txt')

table = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

secret_num = {(2,1,1): 0, (2,2,1): 1, (1,2,2): 2, (4,1,1): 3, (1,3,2): 4, (2,3,1): 5, (1,1,4): 6, (3,1,2): 7, (2,1,3): 8, (1,1,2): 9}

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    num2 = [''] * n
    result = 0
    for i in range(n):
        arr = input()
        for j in range(m):
            num2[i] += table[arr[j]]            # 2 진수로 받기
    # print(num2)

    secret_code = []
    flag = 0
    for x in range(1, n-1):
        for y in range(m*4-2, 0, -1):
            if num2[x][y] == '1' and num2[x-1][y] == '0' and flag == 0:
                flag = 1
                code = ''
            if flag:
                if num2[x-1][y] == '0':
                    code = num2[x][y] + code
                elif len(code) >= 56:
                    secret_code.append(list(code))
                    flag = 0
                    code = ''
                else:
                    flag = 0
                    code = ''

    # print(secret_code)

    code_len = len(secret_code)
    for k in range(code_len):
        cnt0 = 0
        cnt1 = 0
        cnt = []
        # print(code_list)
        for z in secret_code[k]:
            if z == '0':
                if cnt1:
                    cnt.append(cnt1)
                    cnt1 = 0
                cnt0 += 1
            else:
                if cnt0:
                    cnt.append(cnt0)
                    cnt0 = 0
                cnt1 += 1
        if cnt0:
            cnt.append(cnt0)
        if cnt1:
            cnt.append(cnt1)

        # print(cnt)
        cnt_len = len(cnt)
        number = []
        for v in range(0, cnt_len, 4):
            tmp1 = min(cnt[v + 1], cnt[v + 2], cnt[v + 3])
            tmp2 = tuple([cnt[v + 1] // tmp1, cnt[v + 2] // tmp1, cnt[v + 3] // tmp1])
            number.append(secret_num[tmp2])

        # print(number)
        judge = 0
        ans = 0
        for w in range(1, 8):
            ans += number[w-1]
            if w % 2:
                judge += number[w-1] * 3
            else:
                judge += number[w-1]
        judge += number[7]
        ans += number[7]

        if judge % 10:
            ans = 0

        result += ans

    print(f'#{tc+1} {result}')
