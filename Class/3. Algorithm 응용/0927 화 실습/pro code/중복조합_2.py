def H(n, r, k, s):
    if k == r:
        print(t)
    else:
        for i in range(s, n):
            t[k] = a[i]
            H(n, r, k+1, i)

N = 3
R = 2
a = [1, 2, 3]
t = [0] * R
H(N, R, 0, 0)