# def comb(n, r):
#     if r == 0:
#         print(T)
#     else:
#         if n < r:
#             return
#         else:
#             T[r-1] = A[n-1]
#             comb(n-1, r-1)
#             comb(n-1, r)
#
#
# A = list(range(1, 5))
# N = len(A)   # 4
# R = 3
# T = [0] * R
# comb(4, 3)

#---------------------------------------
def comb(n, r):
    if r == 0:
        return 1
    else:
        if n < r:
            return 0
        else:
            return comb(n-1, r-1) + comb(n-1, r)

print(comb(50, 30))