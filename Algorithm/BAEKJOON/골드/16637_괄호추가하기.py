def operator(a, s, b):
    a = int(a)
    b = int(b)

    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == "*":
        return a * b


def dfs(i, ssum):
    global ans

    if i >= n-1:
        if ans < ssum:
            ans = ssum
        return

    # 괄호 없음
    if i+1 < n:
        dfs(i+2, operator(ssum, arr[i], arr[i+1]))
    # 뒤에 괄호 있음
    if i+3 < n:
        bracket = operator(arr[i + 1], arr[i + 2], arr[i + 3])
        dfs(i+4, operator(ssum, arr[i], bracket))

n = int(input())
arr = input()

ans = -2**31
dfs(1, int(arr[0]))

print(ans)