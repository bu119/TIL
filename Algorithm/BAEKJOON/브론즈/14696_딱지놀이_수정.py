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

    cnt = 0
    for k in range(4, 0, -1):
        if cntA[k] != cntB[k]:
            if cntA[k] > cntB[k]:
                print('A')
            else:
                print('B')
            break
        else:
            cnt += 1

    if cnt == 4:
        print('D')