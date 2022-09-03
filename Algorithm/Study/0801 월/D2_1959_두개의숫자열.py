# D2 : 1959. 두 개의 숫자열
t=int(input())
for k in range(t):
    n,m=list(map(int, input().split()))
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    lis=[]
    if n<m :
        for i in range(m-n+1):
            sum=0
            for j in range(n):
                c=A[j]*B[j+i]
                sum=sum+c
            lis.append(sum)
    else:
        for i in range(n-m+1):
            sum=0
            for j in range(m):
                c=B[j]*A[j+i]
                sum=sum+c
            lis.append(sum)
    print(f'#{k+1} {max(lis)}')