# 1974. 스도쿠 검증
t = int(input())
for i in range(t):                      # t 개수 만큼 반복
    list_n = []
    a = 0
    for j in range(9):
        number=list(map(int,input().split()))
        list_n.append(number)
    
    for row1 in list_n:                 # 각 행 확인
        if sorted(row1) == list(range(1,10)):
            a += 0
        else:
            a += 1
    
    for n1 in range(9):
        col = []
        for row2 in list_n:             # 각 열 확인
            col.append(row2[n1])
        if sorted(col) == list(range(1,10)):
            a += 0
        else:
            a += 1

    for row3 in range(0, 9, 3):         # 3 행씩 나눠서 squ에 추가
        for co11 in range(0, 9, 3):     # square 확인
            squ = []
            squ += list_n[0 + row3][co11 : co11 + 3]
            squ += list_n[1 + row3][co11 : co11 + 3]
            squ += list_n[2 + row3][co11 : co11 + 3]

            if sorted(squ) == list(range(1,10)):
                a += 0                  # 모두 통과면 0을 더한다.
            else:
                a += 1

    if a == 0:
        print(f'#{i + 1} 1')            # 모두 통과면 0이 나와서 1을 출력
    else:
        print(f'#{i + 1} 0')
