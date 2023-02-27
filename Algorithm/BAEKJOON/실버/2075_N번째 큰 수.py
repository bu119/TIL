import heapq

n = int(input())

# 메모리 초과
# arr =[]
# for _ in range(n):
#     for i in map(int, input().split()):
#         heapq.heappush(arr, -i)
#
# for j in range(n - 1):
#     heapq.heappop(arr)
#
# print(-arr[0])

arr = list(map(int, input().split()))
heapq.heapify(arr)
for i in range(n-1):
    for num in list(map(int, input().split())):
        if arr[0] < num:
            heapq.heappop(arr)
            heapq.heappush(arr, num)

print(arr[0])



