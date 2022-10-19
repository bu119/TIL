formula = input().split('-')

n = len(formula)
ans = 0

for i in range(n):
    num = map(int, formula[i].split('+'))
    if i == 0:
        ans += sum(num)
    else:
        ans -= sum(num)

print(ans)