import sys
input = sys.stdin.readline
def dfs(v, cnt):
    global ans, flag

    if cnt > ans:
        return

    if v >= n-1:
        flag = 1
        if ans > cnt:
            ans = cnt
        return

    if A[v] == 0:
        return

    for i in range(1, A[v]+1):
        dfs(v+i, cnt + 1)

n = int(input())
A = list(map(int,input().split()))
ans = n
flag = 0
dfs(0,0)

if flag == 0:
    ans = -1

print(ans)