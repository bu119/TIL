t = int(input())
for tc in range(t):
    str1 = input()
    str2 = input()
    n = len(str1)
    for i in range(len(str2)):
        if str2[i:i+n] == str1:
            result = 1
            break
        else:
            result = 0

    print(f'#{tc+1} {result}')