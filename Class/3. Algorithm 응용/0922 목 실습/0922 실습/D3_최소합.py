import sys
sys.stdin = open('testcase/5188_최소합_input.txt')

def dfs(ssum, i, j):
    global ans

    if ans < ssum:
        return

    if i == n-1 and j == n-1:
        if ans > ssum:
            ans = ssum
    else:
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                # ssum += arr[ni][nj]
                dfs(ssum+arr[ni][nj], ni, nj)
                # dfs(ssum, ni, nj)
                # ssum -= arr[ni][nj]

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 1690
    di = [0, 1]
    dj = [1, 0]
    dfs(arr[0][0], 0, 0)
    print(f'#{tc+1} {ans}')
