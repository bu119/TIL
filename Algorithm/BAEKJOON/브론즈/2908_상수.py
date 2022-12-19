a, b = input().split()
A=''
B=''
for i in range(2,-1,-1):
    A += a[i]
    B += b[i]

if A > B:
    print(A)
else:
    print(B)
