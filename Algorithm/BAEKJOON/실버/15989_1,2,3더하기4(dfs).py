def dfs(ssum):
    global n, visited

    if ssum > n:
        return

    if ssum == n:
        check.add(tuple(visited))
        return

    visited[1] += 1
    dfs(ssum + 1)
    visited[1] -= 1

    visited[2] += 1
    dfs(ssum + 2)
    visited[2] -= 1

    visited[3] += 1
    dfs(ssum + 3)
    visited[3] -= 1


t = int(input())

for _ in range(t):
    n = int(input())
    check = set()
    visited = [0,0,0,0]
    dfs(0)
    print(len(check))
