# nㅠn

def perm(n, k):  # k는 깊이
    if n == k:
        print(*p)
    else:
        for i in range(n):
            # if visited[i] == 0:
            #     visited[i] = 1
                p[k] = a[i]
                perm(n, k+1)
                # visited[i] = 0


a = [1, 2, 3]
N = len(a)
p = [0] * N
# visited = [0] * N
perm(N, 0)