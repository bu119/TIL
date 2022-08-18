import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):
    repetition = input()
    result = [repetition[0]]
    top = 0
    for i in range(1, len(repetition)):
        result.append(repetition[i])
        top += 1
        if len(result) > 1 and result[top-1] == result[top]:
            result.pop()
            result.pop()
            top -= 2

    print(f'#{tc+1}', end=' ')

    if len(result):
        print(len(result))
    else:
        print(0)