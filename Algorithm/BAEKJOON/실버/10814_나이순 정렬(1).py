import sys
input=sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    info.append(input().split())

info.sort(key=lambda x: int(x[0]))

for i in info:
    print(' '.join(i))