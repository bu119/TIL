ans = 0

for n in range(9):
    num = int(input())
    if ans < num:
        ans = num
        idx = n+1

print(ans)
print(idx)