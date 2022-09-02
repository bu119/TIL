def paper(num):
    if num < 2:
        return 1
    elif num % 2: # 홀수 규칙
        return paper(num-2) * 4 + 1
    elif num % 2 == 0:  # 짝수 규칙
        return paper(num-2) * 4 - 1

t = int(input())
for tc in range(t):
    n = int(input())
    print(f'#{tc+1} {paper(n//10)}')