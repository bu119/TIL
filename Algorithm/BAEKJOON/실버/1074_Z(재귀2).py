def zzz(x, y, size, num):

    if x == r and y == c:
        print(num)
        exit(0)
    else:
        size //= 2
        for i in range(2):
            for j in range(2):
                nx = x + size * i
                ny = y + size * j
                if nx <= r < nx + size and ny <= c < ny + size:
                    zzz(nx, ny, size, num + (size**2) * (i*2 + j))

n, r, c = map(int, input().split())
zzz(0, 0, 2**n, 0)
