for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:                # 떨어져 있을 때
        print('d')
    elif (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2) or (p2 == x1 and q2 == y1) or (x2 == p1 and q2 == y1):    # 한점
        print('c')
    elif p1 == x2 or x1 == p2 or q1 == y2 or q2 == y1:          # 선
        print('b')
    else:                                                       # 면
        print('a')
