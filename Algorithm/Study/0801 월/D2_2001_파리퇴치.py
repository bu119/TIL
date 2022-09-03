# 2001. 파리 퇴치
t=int(input())
for i in range(t):
    n,m = map(int,input().split())
    lis1=[]
    lis2=[]
    for j in range(n):
        num = map(int,input().split())
        lis1.append(list(num))
    for kc in range(n-m+1):
        for kr in range(n-m+1):
            sum=0
            for lr in range(m):
                for lc in range(m):
                    sum += lis1[lr+kr][kc+lc]
            lis2.append(sum)
    print(f'#{i+1} {max(lis2)}')