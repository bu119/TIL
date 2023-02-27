import sys, heapq
input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]

heapq.heapify(card)

ssum = 0
while len(card) > 1:
    num = heapq.heappop(card) + heapq.heappop(card)
    ssum += num
    heapq.heappush(card, num)

print(ssum)