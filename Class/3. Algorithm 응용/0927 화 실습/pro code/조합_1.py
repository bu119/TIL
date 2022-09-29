def comb(n, r):
    if r == 0:
        print(T)
    elif n < r:
        return
    else:
        T[r - 1] = A[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


A = [1, 2, 3, 4]
N = len(A)
R = 3
T = [0] * R

comb(4, 3)