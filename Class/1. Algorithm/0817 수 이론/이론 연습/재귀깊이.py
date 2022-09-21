def f(i, n):
    if i == n:
        return
    else:
        f(i+1, n)

f(0, 2500)