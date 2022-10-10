def find(n):
    cnt = 4
    if n in square_num:
        return 1
    else:
        for j in square_num:
            if n - j in square_num:
                return 2
            else:
                for k in square_num:
                    if n - j - k in square_num:
                        cnt = 3
    return cnt

n = int(input())
square_num = []
possible = int(n**(1/2)) + 1

for i in range(1, possible):
    square_num.append(i**2)

print(find(n))