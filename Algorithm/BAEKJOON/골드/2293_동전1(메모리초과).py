import sys, copy
sys.setrecursionlimit(10**6)
def dfs(ssum, cnt):
    global visited, num, ans

    if num in visited[cnt]:
        # print(visited)
        return
    else:
        tmp = copy.deepcopy(num)
        visited[cnt].append(tmp)


    if ssum > k:
        return

    if ssum == k:
        ans += 1
        return

    for i in range(n):
        num[i] += 1
        dfs(ssum + coin[i], cnt + 1)
        num[i] -= 1


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

visited = [[] for _ in range(k+1)]
num = [0] * n
ans = 0
dfs(0, 0)
print(ans)
