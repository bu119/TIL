import sys
input=sys.stdin.readline

arr = input().rstrip()
while arr != '.':

    check = ''
    arr = ''.join(arr.split())

    if len(arr) == 1:
        print('yes')
    else:
        for i in arr:
            if i == '(' or i == ')' or i == '[' or i == ']':
                check += i
            n = len(check)
            if n > 1:
                if check[n-2:n] == '()' or check[n-2:n] == '[]':
                    check = check[:n-2]

        if len(check):
            print('no')
        else:
            print('yes')

    arr = input().rstrip()