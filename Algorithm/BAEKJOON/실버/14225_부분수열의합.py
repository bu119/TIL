n = int(input())
s = sorted(map(int, input().split()))
ssum = 1
for i in range(n):
    print(ssum, s[i])
    if ssum < s[i]:
        print('if문 들어옴')
        break
    ssum += s[i]
print(ssum)