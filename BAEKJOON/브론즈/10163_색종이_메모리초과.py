arr = []
n = int(input())
for tc in range(n):
    tmp = []
    size = list(map(int, input().split()))
    for i in range(size[0], size[0] + size[2]):
        for j in range(size[1], size[1] + size[3]):
            tmp.append((j, i))
    arr.append(tmp)

for k in range(n-1):
    result = set(arr[k])
    for minus in range(k+1, n):
        result -= set(arr[minus])
    print(len(result))

print(len(arr[-1]))


