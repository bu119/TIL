def powerset(n, k):
    if n == k:
        # print(b)
        for i in range(n):
            if b[i] == 1:
                print(a[i], end=' ')
        print()
    else:
        b[k] = 1
        powerset(n, k+1)
        b[k] = 0
        powerset(n, k+1)

a = [1, 2, 3]
b = [0] * 3
N = len(a)
powerset(N, 0)