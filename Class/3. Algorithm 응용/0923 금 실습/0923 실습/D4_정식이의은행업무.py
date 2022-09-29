def ch2_10(arr):
    ch_10 = 0
    n = len(arr)
    for k in range(n):
        ch_10 += (arr[n-1-k] * (2**k))
    return ch_10

def ch3_10(arr):
    ch_10 = 0
    n = len(arr)
    for k in range(n):
        ch_10 += (arr[n-1-k] * (3**k))
    return ch_10


t = int(input())
for tc in range(t):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))
    number2 = []
    number3 = []

    for i in range(len(num2)):
        if num2[i]:
            num2[i] = 0
            number2.append(ch2_10(num2))
            num2[i] = 1
        else:
            num2[i] = 1
            number2.append(ch2_10(num2))
            num2[i] = 0

    for j in range(len(num3)):
        if num3[j] == 0:
            num3[j] = 1
            tmp1 = ch3_10(num3)
            num3[j] = 2
            tmp2 = ch3_10(num3)
            num3[j] = 0
        elif num3[j] == 1:
            num3[j] = 2
            tmp1 = ch3_10(num3)
            num3[j] = 0
            tmp2 = ch3_10(num3)
            num3[j] = 1
        else:
            num3[j] = 0
            tmp1 = ch3_10(num3)
            num3[j] = 1
            tmp2 = ch3_10(num3)
            num3[j] = 2
        if tmp1 in number2:
            print(f'#{tc+1} {tmp1}')
            break
        elif tmp2 in number2:
            print(f'#{tc+1} {tmp2}')
            break
        else:
            number3.append(tmp1)
            number3.append(tmp2)