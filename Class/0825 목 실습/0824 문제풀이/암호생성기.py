T = 10
for tc in range(1, T + 1):
    no = int(input())
    Q = list(map(int, input().split()))

    count = 0
    temp = 0

    while True:
        temp = Q.pop(0)
        temp -= count % 5 + 1
        if temp < 0: temp = 0

        Q.append(temp)
        count += 1
        if temp == 0:
            break

    print("#{}".format(tc), end=" ")
    for i in range(len(Q)):
        print(Q[i], end=" ")
    print()