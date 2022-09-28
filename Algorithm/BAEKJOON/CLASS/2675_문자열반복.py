t = int(input())
for tc in range(t):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(i * r, end='')
    print()
