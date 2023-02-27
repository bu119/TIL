n = int(input())
k = int(input())
pos = sorted(map(int, input().split()))

if n <= k:
    print(0)
else:
    dif = []
    # 인접한 센서들 간의 거리의 차
    for i in range(n-1):
        dif.append(pos[i+1]-pos[i])
    dif.sort()
    print(sum(dif[:n-k]))