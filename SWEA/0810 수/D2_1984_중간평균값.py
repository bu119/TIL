#1984. 중간 평균값 구하기
t = int(input())
for i in range(t):
    numbers = list(map(int,input().split()))
    numbers.sort()
    avg = sum(numbers[1:-1]) / len(numbers[1:-1])    # 최대 수와 최소 수를 제외
    print(f'#{i+1} {round(avg)}')