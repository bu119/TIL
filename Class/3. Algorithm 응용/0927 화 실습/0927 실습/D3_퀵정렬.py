def partition(l, r):
    p = num[l]
    i = l
    j = r
    while i <= j:
        while i <= j and num[i] <= p:
            i += 1
        while i <= j and num[j] >= p:
            j -= 1

        if i < j:
            num[i], num[j] = num[j], num[i]

    num[l], num[j] = num[j], num[l]
    return j

def quick(l, r):
    if l < r:
        s = partition(l,r)
        quick(l, s-1)
        quick(s+1, r)


t = int(input())
for tc in range(t):
    n = int(input())
    num = list(map(int,input().split()))

    quick(0, n-1)
    print(f'#{tc+1} {num[n//2]}')