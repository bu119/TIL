import sys
input = sys.stdin.readline


def dfs(k, idx):
    global ans
    if k == n//2:
        startT = 0
        linkT = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    startT += arr[i][j]
                elif not visited[i] and not visited[j]:
                    linkT += arr[i][j]

        if abs(startT-linkT) < ans:
            ans = abs(startT-linkT)
        return
    for z in range(idx, n):
        if not visited[z]:
            visited[z] = 1
            dfs(k+1, idx+1)
            visited[z] = 0


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [0]*n
ans = 100
dfs(0, 0)

print(ans)