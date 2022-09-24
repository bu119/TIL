import sys
sys.stdin = open('testcase/input_최소생산비용.txt')

def dfs(x, i, ssum):
    global ans

    if x == n-1:
        if ans > ssum:
            ans = ssum
        return

    if ans < ssum:
        return

    for y in range(n):
        if visited[y] == 0:
            visited[y] = 1
            dfs(x+1, y, ssum + cost[x+1][y])
            visited[y] = 0


t = int(input())
for tc in range(t):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    ans = 99 * n
    for i in range(n):              # 시작 인덱스
        visited = [0] * n
        visited[i] = 1
        dfs(0, i, cost[0][i])
    print(f'#{tc+1} {ans}')