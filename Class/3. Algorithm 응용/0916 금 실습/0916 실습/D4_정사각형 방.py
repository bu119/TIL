import sys
sys.stdin = open('testcase/input_정사각형.txt')

def bfs(i, j):
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        x, y = q.pop(0)
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == arr[x][y] + 1:
                visited[ni][nj] = visited[x][y] + 1
                q.append((ni, nj))
    return visited[x][y]

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0]*n for _ in range(n)]
    di = [0, 1, 0, -1]  # 우 부터 시계방향
    dj = [1, 0, -1, 0]
    max_cnt = 0

    for i in range(n):
        for j in range(n):
            cnt = bfs(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                ans = arr[i][j]
            elif max_cnt == cnt and ans > arr[i][j]:
                ans = arr[i][j]
    print(f'#{tc+1} {ans} {max_cnt}')