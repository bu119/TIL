# 1970. 쉬운 거스름돈
t = int(input())
for i in range(t):
    n = int(input())
    money = []
    for j in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:    # 돈 종류의 금액이 큰 순서대로 반복 시행
        money.append(n // j)          # 한 종류의 돈으로 나눈 몫을 빈 리스트에 추가
        n = n % j                     # 같은 종류의 돈으로 나눈 나머지를 n으로 바꾸고 다음 돈에 적용

    mon =' '.join(map(str, money))    # 리스트로 이루어진 돈의 개수를 문자열로 변환
    print(f'#{i+1}\n{mon}')