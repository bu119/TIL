def pizza():
    Q = []
    for i in range(1, N + 1):  # 화덕에 N개 피자 넣기
        Q.append(i)

    idx = N + 1  # 아직 화덕에 넣지 않은 첫번째 피자
    while len(Q) > 1:
        t = Q.pop(0)  # deQ
        arr[t] = arr[t] // 2  # 치즈 반으로 줄이기
        # 치즈가 남아 있으면 -> Q에 넣기
        if arr[t] != 0:
            Q.append(t)
        # 치즈가 다 녹았을 때 -> 총 피자수 확인
        elif idx <= M:
            Q.append(idx)
            idx += 1

    return Q[0]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕크기, 피자갯수
    arr = [0] + list(map(int, input().split()))  # 인덱스 1번부터
    print(f'#{tc} {pizza()}')