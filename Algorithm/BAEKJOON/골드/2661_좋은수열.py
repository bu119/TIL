# 같은 부분 수열이 존재하는 지 확인
def check(arr):
    for i in range(1, len(arr)//2 + 1):
        if arr[-i:] == arr[-(2*i):-i]:
            return 1
    return 0


def dfs(sequence):

    if len(sequence) == n:
        print(sequence)
        exit(0)

    for k in ['1', '2', '3']:
        if sequence[-1] != k and not check(sequence+k):
            dfs(sequence+k)


n = int(input())
sequence = '1'

dfs(sequence)



