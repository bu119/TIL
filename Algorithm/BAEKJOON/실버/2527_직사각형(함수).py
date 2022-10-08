for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    x = max(x1, x2)
    p = min(p1, p2)
    y = max(y1, y2)
    q = min(q1, q2)

    if x > p or y > q:          # 떨어져 있을 때
        print('d')
    elif x == p and y == q:     # 점
        print('c')
    elif x == p or y == q:      # 선
        print('b')
    else:                       # 사각형
        print('a')