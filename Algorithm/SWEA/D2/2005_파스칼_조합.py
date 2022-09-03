# 2005. 파스칼의 삼각형

# 팩토리얼
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# 파스칼 삼각형: 확률과통계- 이항정리의 이항계수 이용
def pascal(n):                     # 파스칼 n번째 줄 출력
    pasc = []
    if n == 1:                     # 1번째 줄 1
        return '1'
    else:                                          # 2번째 줄부터 1 1
        for r in range(n):                         # 2번째 줄이면 1C0, 1C1 # 3번째 줄이면 2C0, 2C1, 2C2
            num = factorial(n-1)                   # 순열과 조합의 조합 분자 계산: n! - nCr이면 n! / r!(n-r)!
            den = factorial(r) * factorial(n-r-1)  # 조합 분모 계산: r!/(n-r)!
            pasc.append(int(num/den))              # 리스트 형식으로 추가 [1, 3, 3, 1]
        return ' '.join(map(str, pasc))            # 숫자 리스트를 문자열로 변환

t = int(input())
for i in range(t):
    num = int(input())
    print(f'#{i+1}')
    for j in range(1, num+1):        # 파스칼 삼각형의 1번 줄부터 num줄 까지 출력
        print(pascal(j))