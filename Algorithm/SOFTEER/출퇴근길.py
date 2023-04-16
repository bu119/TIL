def dfs1(v, visited, string):
    if v == t:
        check1.add(string)
        return

    for w in adj1[v]:
        if visited[w] != 1 and w not in string:
            visited[w] = 1
            dfs1(w, visited, string + str(w))
            visited[w] = 0

    return


def dfs2(v, visited, string):
    if v == t:
        check2.add(string)
        return

    for w in adj1[v]:
        if visited[w] != 1 and w not in string:
            visited[w] = 1
            dfs2(w, visited, string + str(w))
            visited[w] = 0

    return


n, m = map(int, input().split())
adj1 = [[] for _ in range(n + 1)]
adj2 = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj1[x].append(y)
    # 반대방향
    adj2[y].append(x)
s, t = map(int, input().split())
check1 = set()
check2 = set()
visitedS = [0] * (n + 1)
visitedT = [0] * (n + 1)
dfs1(s, visitedS, str(s))
dfs2(s, visitedT, str(s))

print(check1)
print(check2)
print(len(check1 & check1))