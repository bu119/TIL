T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [] # 2차원 배열 입력받기
    for n in range(N):
        arr.append(list(map(int, input())))

    d = N//2 # N의 중간값
    total = sum(arr[d]) # 농작물 수익    # 중간행 따로 구함

    for i in range(d): # 끝에서 부터 안쪽으로 더해줌
        temp1 = arr[i][d-i : d+1+i] # 슬라이싱 할 때 원하는 숫자보다 1더해줘야한다
        temp2 = arr[N-1-i][d-i : d+1+i]
        total += sum(temp1) + sum(temp2)

    print(f'#{tc} {total}')