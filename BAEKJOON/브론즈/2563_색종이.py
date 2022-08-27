arr = [list([0]*101) for _ in range(101)]
cnt = 0
n = int(input())
for tc in range(n):
    size = list(map(int, input().split()))
    for i in range(size[0], size[0] + 10):
        for j in range(size[1], size[1] + 10):
            arr[j][i] = 1

for row in range(101):
    for col in range(101):
        if arr[row][col] == 1:
            cnt += 1

print(cnt)