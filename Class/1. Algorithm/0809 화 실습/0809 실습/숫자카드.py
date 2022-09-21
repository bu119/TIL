t = int(input())
for tc in range(t):
    n = int(input())
    a = list(map(int, input()))

    count = [0] * 10

    max_a = 0
    for i in range(n):
        count[a[i]] += 1     # 0 ~ 9까지의 각 숫자가 인덱스가 되어 개수를 값으로 할당한다.

    max_count = 0
    num = 0
    for j in range(10):
        if max_count < count[j]:      # 개수의 최대값 찾기
            max_count = count[j]      # 최대 장수
            num = j                   # 그때의 인덱스 즉, 카드의 숫자

    for k in range(10):
        if max_count == count[k]:     # 최대 장수가 중복 존재하면
            if num < k:               # 앞서 구한 j숫자보다 k숫자가 크면 num=k
                num = k

    print(f'#{tc+1} {num} {max_count}')
