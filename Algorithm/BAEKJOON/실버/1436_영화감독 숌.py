# 666, 1666, 2666, ..., 6660, 6661, 6662, ..., 9666

n = int(input())
i = 0
num = 665
while i < n:
    num += 1
    if '666' in str(num):
        i += 1

print(num)