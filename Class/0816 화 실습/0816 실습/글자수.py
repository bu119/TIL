import sys
sys.stdin = open("글자수_input.txt.", "r")

t = int(input())
for tc in range(t):
    str1 = input()
    str2 = input()
    dic_str2 = {}
    for i in str2:
        if i in dic_str2:
            dic_str2[i] += 1
        else:
            dic_str2[i] = 1

    max_cnt = 0
    for j in set(str1):
        if max_cnt < dic_str2[j]:
            max_cnt = dic_str2[j]
    print(f'#{tc+1} {max_cnt}')



