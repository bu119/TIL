import sys
sys.stdin = open('testcase/input_배열최소합 .txt')

def dfs(r, ssum):
    global ans

    if r == n-1:
        if ans > ssum:
            ans = ssum
            return

    if ans < ssum:
        return

    for v in range(n):
        if not visited[v]:
            visited[v] = 1
            dfs(r+1, ssum + arr[r+1][v])
            visited[v] = 0


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 10 * n

    for i in range(n):
        visited = [0] * n
        visited[i] = 1
        dfs(0, arr[0][i])
    print(f'#{tc+1} {ans}')