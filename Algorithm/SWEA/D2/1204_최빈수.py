# 1204. 최빈수 구하기
t = int(input())
for tc in range(t):
    n = int(input())
    grade = list(map(int, input().split()))
    num = []
    for i in set(grade):
        num.append((grade.count(i), i))     # (빈도수, 숫자)
    num.sort(reverse=True)         # 정렬할 때 같은 수가 나오면 다음 인덱스 수가 큰 순서대로 출력
    print(f'#{n} {num[0][1]}')

