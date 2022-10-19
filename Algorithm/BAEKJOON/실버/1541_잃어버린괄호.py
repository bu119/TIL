formula = list(input()) + ['+']
n = len(formula)
ans = 0
num = ''
minus = 0

for i in range(n):

    if formula[i].isdigit():
        num += formula[i]
    else:
        if minus:
            ans -= int(num)
        else:
            ans += int(num)

        if formula[i] == '-':
            minus = 1

        num = ''
print(ans)