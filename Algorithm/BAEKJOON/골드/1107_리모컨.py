def close_num(num):             # 가까운 숫자 찾기
    if o_x == 1:
        return o_num[0]

    if num < o_num[0]:
        return o_num[0]

    if o_num[-1] < num:
        return o_num[-1]

    for x in range(1, o_x):
        if o_num[x-1] < num < o_num[x]:
            if num - o_num[x-1] < num - o_num[x]:
                return o_num[x-1]
            elif num - o_num[x-1] > num - o_num[x]:
                return o_num[x]
            else:
                return o_num[x-1], o_num[x]

def find_num(arr):              # 숫자 찾기
    numb = 0
    nn = len(arr)
    for x in range(nn):
        numb += arr[x] * (10**(nn-1-x))
    return numb


n = list(map(int, input()))
m = int(input())
if m:
    x_num = list(map(int, input().split()))

number = find_num(n)
# print(number)

o_num = list(range(10))
o_x = 10-m
cnt = len(n)
num = []

if cnt == 3 and n[0] == 1 and n[1] == 0:
    print(n[2])
else:
    for i in range(m):
        o_num.remove(x_num[i])

    if cnt == 1:
        new = close_num(n[0])
        print(abs(n[0] - new) + cnt)

    else:
        for j in range(len(n)):
            if n[j] in o_num:
                num.append(n[j])
            else:
                num.append(close_num(n[j]))

        new = find_num(num)

        print(abs(number-new)+cnt)
