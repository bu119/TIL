t = int(input())
for tc in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    result = 0
    for i in range(n):          # 0번째 인덱스 부터 순서대로 다른 인덱스와 비교
        max_h = n - 1 - i       # 낙차의 최대 높이
        for j in range(i + 1, n):         # 비교 대상
            if height[i] <= height[j]:    # 기준 높이 보다 크면
                max_h -= 1                # 낙차 감소

        if result < max_h:     # 기준 높이의 낙차 값이 크면
            result = max_h     # 결과 값 대체

    print(f'#{tc+1} {result}')






    # max_h = 0
    # num = 0
    # for i in range(n):                # 최대값
    #     if max_h < height[i]:
    #         max_h = height[i]
    #         num = i
    # cnt = 0
    # for j in range(n):               # 최대 높이를 가진 상자의 개수
    #     if max_h == height[j]:
    #         cnt += 1
    #
    # high = n - num - cnt
    # print(f'#{tc+1} {high}')
    #


