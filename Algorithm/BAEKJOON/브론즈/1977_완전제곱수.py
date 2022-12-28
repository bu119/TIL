m = int(input())
n = int(input())
ans = []
for i in range(1,10001):
    num = i * i
    if m <= num and num <= n:
        ans.append(num)

    if n < num:
        break

if ans:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)