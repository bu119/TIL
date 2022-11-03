def dfs(i, j, ):




arr = [input().split() for _ in range(5)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(5):
    for j in range(5):
        dfs(i,j)