channel = int(input())
broken_n = int(input())
if broken_n:
    broken = input().split()
else:
    broken = []

cnt = abs(channel - 100)
c = len(str(channel))

for number in range(1000001):
    flag = 1
    for num in str(number):
        if num in broken:
            flag = 0
            break

    if flag:
        cnt = min(cnt, abs(number - channel) + len(str(number)))

print(cnt)
