string = input() # mirkovC4nizCC44
explosion = list(input()) # C4
m = len(explosion)
last_char = explosion[m-1]

stack = []
for char in string:
    stack.append(char)
    if last_char == char and stack[-m:] == explosion:
        del stack[-m:]

if stack:
    print("".join(stack))
else:
    print("FRULA")