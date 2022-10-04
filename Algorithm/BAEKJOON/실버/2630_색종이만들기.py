n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size = n*n
while n > 0:

    for i in range(n//2):
        for j in range(n//2):
            if arr[i][j] == 1:
                b +=1
            else:
                w +=1