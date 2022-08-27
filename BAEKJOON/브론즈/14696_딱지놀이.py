n = int(input())
for tc in range(n):
    cntA = [0] * 5
    cntB = [0] * 5
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(a[0]):
        cntA[a[i + 1]] += 1

    for j in range(b[0]):
        cntB[b[j + 1]] += 1

    if cntA[4] != cntB[4]:
        if cntA[4] > cntB[4]:
            print('A')
        else:
            print('B')
    elif cntA[3] != cntB[3]:
        if cntA[3] > cntB[3]:
            print('A')
        else:
            print('B')
    elif cntA[2] != cntB[2]:
        if cntA[2] > cntB[2]:
            print('A')
        else:
            print('B')
    elif cntA[1] != cntB[1]:
        if cntA[1] > cntB[1]:
            print('A')
        else:
            print('B')
    else:
        print('D')