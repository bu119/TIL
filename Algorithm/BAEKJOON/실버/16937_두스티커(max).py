from itertools import permutations
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
sticker = []

for _ in range(n):
    r, c = map(int, input().split())
    if (r <= h and c <= w) or (c <= h and r <= w):
        sticker.append((r, c))

choice = list(permutations(sticker, 2))

ans = 0
for a, b in choice:
    x, y = a
    p, q = b
    area = 0
    if (x + p <= h and max(y, q) <= w) or (max(x, p) <= h and y + q <= w):
        area = x * y + p * q
    elif (y + p <= h and max(x, q) <= w) or (max(y, p) <= h and x + q <= w):
        area = x * y + p * q
    elif (y + q <= h and max(x, p) <= w) or (max(y, q) <= h and x + p <= w):
        area = x * y + p * q
    elif (x + q <= h and max(y, p) <= w) or (max(x, q) <= h and y + p <= w):
        area = x * y + p * q

    if ans < area:
        ans = area

print(ans)