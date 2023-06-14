s = list(input())
t = list(input())
cnt = len(t)
def dfs(arr):
    global t
    if arr == t:
        print(1)
        exit(0)

    if len(arr) == len(t):
        return

    arr.append('A')
    dfs(arr)
    arr.pop()

    arr.append('B')
    arr.reverse()
    dfs(arr)
    arr.reverse()
    arr.pop()


dfs(s)
print(0)