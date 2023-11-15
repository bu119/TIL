string = input() # mirkovC4nizCC44
explosion = input() # C4

while explosion in string:
    string = string.replace(explosion, "")

if string:
    print(string) # mirkovniz
else:
    print("FRULA")