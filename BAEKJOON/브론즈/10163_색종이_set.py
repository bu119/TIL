arr = []
n = int(input())
for tc in range(n):
    tmp = []
    size = list(map(int, input().split()))
    for i in range(size[0], size[0] + size[2]):
        for j in range(size[1], size[1] + size[3]):
            tmp.add((j, i))
    arr.append(tmp)

for k in range(n-1):
    for minus in range(k+1, n):
        same = arr[k] & arr[minus]
        if same:
            arr[k] -= same
    print(len(arr[k]))

print(len(arr[-1]))