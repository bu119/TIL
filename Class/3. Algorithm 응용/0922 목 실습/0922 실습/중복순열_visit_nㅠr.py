# nㅠr

def perm(n, r, k):  # k는 깊이
    if r == k:
        print(*p)
    else:
        for i in range(n):
            # if visited[i] == 0:
            #     visited[i] = 1
                p[k] = a[i]
                perm(n, r, k+1)
                # visited[i] = 0


a = [1, 2, 3]
N = len(a)
R = 2
p = [0] * R
# visited = [0] * N
perm(N, R, 0)