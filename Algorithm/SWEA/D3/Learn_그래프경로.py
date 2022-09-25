import sys
sys.stdin = open('testcase/input_그래프경로.txt')

def dfs(S):
    global flag

    visited[S] = 1

    if S == G:
        flag = 1

    for w in arr[S]:
        if not visited[w]:
            dfs(w)

t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        arr[s].append(e)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    flag = 0
    dfs(S)
    print(f'#{tc+1} {flag}')
