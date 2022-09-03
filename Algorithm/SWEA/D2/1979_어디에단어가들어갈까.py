# 1979. 어디에단어가들어갈수있을까
t=int(input())
for i in range(t):
    lis1=[]
    sum=0
    n,k=map(int,input().split())
    for j in range(n):       
        num=input()
        lis1.append(num.split())
        row=num.replace(' ','').split('0')
        sum = sum + row.count('1' * k)
    for r in range(n):
        num2=' '
        for c in range(n):
            num2 = num2 + lis1[c][r]
        col = num2.replace(' ','').split('0')
        sum = sum + col.count('1' * k)
    print(f'#{i+1} {sum}')