num = list(map(int,input().split()))
total = 0
for i in num:
    total += i*i

print(total % 10)