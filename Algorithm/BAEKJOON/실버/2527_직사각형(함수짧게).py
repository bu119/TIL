for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    x = min(p1, p2) - max(x1, x2)
    y = min(q1, q2) - max(y1, y2)

    if x < 0 or y < 0:
        print('d')
    elif x == 0 and y == 0:
        print('c')
    elif x == 0 or y == 0:
        print('b')
    else:
        print('a')