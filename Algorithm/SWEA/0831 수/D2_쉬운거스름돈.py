import sys
sys.stdin = open('testcase/거스름돈_input.txt')

type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# 1. 바로 프린트
t = int(input())
for tc in range(t):
    money = int(input())

    print(f'#{tc+1}')

    for i in range(len(type)):
        print(money // type[i], end=' ')
        money = money % type[i]
    print()

# 2. append, join
# t = int(input())
# for tc in range(t):
#     money = int(input())
#     cnt = []
#     for i in range(len(type)):
#         cnt.append(money // type[i])
#         money = money % type[i]
#     result = ' '.join(map(str, cnt))
#     print(f'#{tc+1}\n{result}')