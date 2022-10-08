for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if y1 < y2:         # 첫 번째 사각형이 아래 위치
        if p1 < x2 or q1 < y2 or p2 < x1:                # 죄우로 떨어져 있을 때
            print('d')
        elif (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2):    # 좌우 한점
            print('c')
        elif p1 == x2 or x1 == p2 or q1 == y2:                      # 좌우 선, 아래위 선
            print('b')
        else:                                                       # 사각형
            print('a')

    else:               # 두 번째 사각형이 아래 위치
        if p2 < x1 or q2 < y1 or p1 < x2:
            print('d')
        elif (p2 == x1 and q2 == y1) or (x2 == p1 and q2 == y1):
            print('c')
        elif p2 == x1 or x2 == p1 or q2 == y1:
            print('b')
        else:
            print('a')