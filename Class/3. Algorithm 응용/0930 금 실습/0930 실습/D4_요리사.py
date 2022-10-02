import sys
sys.stdin = open('testcase/input_요리사.txt')

def dfs(k, cnt):
    global ans

    if cnt == n//2:
        sy1 = sy2 = 0

        for i in range(n-1):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    sy1 += synergy[i][j] + synergy[j][i]
                elif not visited[i] and not visited[j]:
                    sy2 += synergy[i][j] + synergy[j][i]

        ans = min(ans, abs(sy1 - sy2))
        return

    for x in range(k, n):
        if not visited[x]:
            visited[x] = 1
            dfs(x+1, cnt+1)
            visited[x] = 0

t = int(input())
for tc in range(t):
    n = int(input())        # 식재료 수
    synergy = [list(map(int, input().split())) for _ in range(n)]

    visited = [0] * n

    ans = 40000
    dfs(0, 0)
    print(f'#{tc+1} {ans}')