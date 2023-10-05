# def binary_search():




n = int(input())
k = int(input())

arrB = []
for i in range(1,n+1):
    for j in range(1,n+1):
        arrB.append(i*j)
arrB.sort()

print(arrB[k-1])
