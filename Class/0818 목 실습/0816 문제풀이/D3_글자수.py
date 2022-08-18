T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    # dict 초기화
    my_dict = {}
    # dict를 이용해서 중복제거
    for key in set(str1):
        my_dict[key] = 0

    # 카운팅
    for key in str2:
        if key in my_dict:
            my_dict[key] += 1

    # 최대값
    ans = 0
    for value in my_dict.values():
        if ans < value:
            ans = value

    print(f'#{tc} {ans}')