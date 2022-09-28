arr = input()
arr = arr.upper()
set_str = set(arr)

max_cnt = 0
max_str = []
for i in set_str:
    cnt = arr.count(i)
    if max_cnt < cnt:
        max_str = []
        max_cnt = cnt
        max_str.append(i)
    elif max_cnt == cnt:
        max_str.append(i)

if len(max_str) > 1:
    print('?')
else:
    print(*max_str)