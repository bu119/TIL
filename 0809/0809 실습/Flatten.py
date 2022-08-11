# 가로 100 / 높이 1-100 / 덤프 1-1000
import sys
sys.stdin = open("input.txt", "r")

for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    min_h = 100
    max_h = 1

    for i in range(dump):

        for j in range(100):
            # 최대 값
            if max_h < box[j]:
                max_h = box[j]
                max_idx = j      # 최대값 인덱스
            # 최소 값
            if min_h > box[j]:
                min_h = box[j]
                min_idx = j      # 최소값 인덱스

        if max_h == min_h:
            break

        box[max_idx] -= 1
        box[min_idx] += 1

    for k in range(100):
        # 최대 값
        if max_h < box[k]:
            max_h = box[k]
        # 최소 값
        if min_h > box[k]:
            min_h = box[k]

    # for k in range(100):
    #     # 최대 값
    #     if box[max_idx] < box[k]:
    #         max_hi = box[k]
    #     # 최소 값
    #     if box[min_idx] > box[k]:
    #         min_hi = box[k]

    print(f'#{tc + 1} {max_h - min_h}')

    # print(f'#{tc + 1} {box[max_idx] - box[min_idx]}')






