t = int(input())
for tc in range(t):
    OX = input()
    n = len(OX)
    ans = 0
    score = 0
    for i in range(n):
        if OX[i] == 'O':
            score += 1
        else:
            score = 0

        ans += score
    print(ans)