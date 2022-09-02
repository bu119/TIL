def paper(n):
    if n < 2:
        return 1
    else:
        return paper(n-1) + paper(n-2) * 2  # 점화식 f(n) = f(n-1) + f(n-2) * 2

t = int(input())
for tc in range(t):
    n = int(input())
    print(f'#{tc+1} {paper(n//10)}')
