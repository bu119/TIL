import sys

input = sys.stdin.readline
n = int(input())
people = {}
num = 0
for _ in range(n):
    x, a = map(int, input().split())
    people[x] = a
    num += a

ssum = 0
for key in sorted(people):
    ssum += people[key]
    if ssum >= num/2:
        print(key)
        break