# nPn
def perm(n, k):  # k는 깊이
    if n == k:
        print(*p)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k+1)
                visited[i] = 0


# a = [1, 2, 3]
# N = len(a)
# p = [0] * N
# visited = [0] * N
# perm(N, 0)
# 고정시키는 방법
a = [1, 2, 3, 4, 5]
N = len(a)
p = [0] * (N+1)   # 하나크게
p[0] = p[N] = a[0]  # 맨앞돠 맨뒤에 고정
visited = [0] * N
visited[0] = 1
perm(N, 1)