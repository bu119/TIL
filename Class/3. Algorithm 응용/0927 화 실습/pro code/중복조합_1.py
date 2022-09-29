def H(n, r):
    if r == 0:
        print(T)
    elif n == 0:
        return
    else:
        T[r - 1] = A[n - 1]
        H(n, r - 1)
        H(n - 1, r)


A = [1, 2, 3, 4]
N = len(A)
R = 3
T = [0] * R

H(4, 3)