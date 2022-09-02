arr = []
for t in range(4):
    tmp = list(map(int, input().split()))
    for i in range(tmp[0], tmp[2]):
        for j in range(tmp[1], tmp[3]):
            arr.append((i, j))

print(len(set(arr)))