n = int(input())
for tc in range(n):
    cntA = [0] * 5
    cntB = [0] * 5
    num_A, *a = map(int, input().split())
    num_B, *b = map(int, input().split())

    for i in range(num_A):
        cntA[a[i]] += 1
    for j in range(num_B):
        cntB[b[j]] += 1

    cntD = 0
    for k in range(4, 0, -1):
        if cntA[k] > cntB[k]:
            print('A')
            break
        elif cntA[k] < cntB[k]:
            print('B')
            break
        else:
            cntD += 1

    if cntD == 4:
        print('D')