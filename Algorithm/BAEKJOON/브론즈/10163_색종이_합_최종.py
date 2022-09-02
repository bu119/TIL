arr = [list([0]*1001) for _ in range(1001)]

n = int(input())
for tc in range(n):
    tmp = []
    size = list(map(int, input().split()))
    for i in range(size[0], size[0] + size[2]):
        for j in range(size[1], size[1] + size[3]):
            arr[j][i] = 1 + tc

cnt = [0] * (n + 1)
for row in range(1001):
    for col in range(1001):
        cnt[arr[row][col]] += 1

for k in range(1, n+1):
    print(cnt[k])