def counting_sort(a, b, k):
    c = [0] * (k + 1)
    # 카운팅
    for i in range(len(a)):
        c[a[i]] += 1

    # 누적
    for i in range(1, len(c)):
        c[i] += a[i-1]

    # 자리 찾기
    for i in range(len(b)-1, -1, -1):
        c[a[i]] -= 1
        b[c[a[i]]] = a[i]


a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)
counting_sort(a, b, 4)
print(a)
print(b)


