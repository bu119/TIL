T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = int(input())

    '''
    cut = 0

    길이를 모를 때는 while문을 돌리면서 count += 1 을 하면 구할 수 있음
    while num > 0:
    num //= 10
    '''

    # 카운팅
    count = [0] * 10
    for i in range(N):
        count[num % 10] += 1
        num //= 10

    # 최대값의 인덱스
    max_idx = 0
    for i in range(1, 10):
        if count[max_idx] <= count[i]:
            max_idx = i

    print(f'#{tc} {max_idx} {count[max_idx]}')