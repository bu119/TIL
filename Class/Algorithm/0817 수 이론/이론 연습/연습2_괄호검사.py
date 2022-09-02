def check_matching(data):
    for i in range(len(data)):
        # 왼쪽 괄호 일때 : push
        if data[i] == '(':           # 괄호의 종류가 많아지면 or
            stack.append(data[i])
        # 오른쪽 괄호 일때 : pop
        elif data[i] == ')':        # {, [
            if len(stack) == 0:
                return False
            else:
                stack.pop()        # 비교 추가

    # stack에 남아 있으면 False
    if stack:
        return False
    else:
        return True


stack = []
str1 = '( )( )((( )))'
srt2 = '((( )((((( )( )((( )( ))((( ))))))'

print(check_matching(str1))