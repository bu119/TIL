a = [1, 2, 3, 4]
N = 4
for i in range(0, N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            print(a[i], a[j], a[k])

# ------------------------------------
def comb(n, r, k, s):
    if k == r:
        print(t)
    else:
        for i in range(s, n - r + 1 + k):
            t[k] = a[i]
            comb(n, r, k+1, i+1)

N = 4
R = 3
a = [1, 2, 3, 4]
t = [0] * R
comb(N, R, 0, 0)