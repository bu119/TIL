import sys, heapq
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()
end = [time[0][1]]

cnt = 0
for i in range(1, n):
    if end[0] <= time[i][0]:
        heapq.heappop(end)
        heapq.heappush(end, time[i][1])
    else:
        heapq.heappush(end, time[i][1])

print(len(end))