n = int(input())
m = int(input())

s = input()
# p = 'IOI'
# for i in range(1,n):
#     p += 'OI'

# size = len(p)
cnt = 0
# for j in range(m-size+1):
#     if s[j:j+size] == p:
#         cnt += 1
#
# print(cnt)
ans = 0
i = 0
while i < (m - 1):
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(ans)