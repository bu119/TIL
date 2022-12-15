import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_v = price[-1]
    profit = 0
    for i in range(n-2, -1, -1):
        if price[i] > max_v:
            max_v = price[i]
        else:
            profit += max_v - price[i]

    print(profit)

