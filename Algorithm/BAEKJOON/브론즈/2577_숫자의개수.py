num = 1
for i in range(3):
    num *= int(input())

number = str(num)
check = list(map(str, range(10)))

for j in check:
    print(number.count(j))