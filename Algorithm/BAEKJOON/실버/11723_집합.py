import sys
input = sys.stdin.readline

s = set()
m = int(input())
for _ in range(m):
    op = input().rstrip()

    if op == 'all':
        s = set(range(1,21))
    elif op == 'empty':
        s = set()
    else:
        oper, x = op.split()
        x = int(x)

        if oper == 'add':
            s.add(x)
        elif oper == 'remove':
            if x in s:
                s.discard(x)
        elif oper == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)