# 같은 부분 수열이 존재하는 지 확인
def check(arr):
    for i in range(1, len(arr)//2 + 1):
        if arr[-i:] == arr[-(2*i):-i]:
            return 0
    return 1


def dfs(sequence, cnt):

    if cnt == n:
        print(sequence)
        exit(0)

    for k in '123':
        if sequence[-1] != k and check(sequence+k):
            dfs(sequence+k, cnt+1)


n = int(input())
dfs('1', 1)