import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    grade = [list(map(int,input().split())) for _ in range(n)]
    grade.sort()
    # 높은 순위 저장
    top = grade[0][1]
    # 작은 수가 높은 순위
    for i in range(1, n):
        if grade[i][1] < top:
            # 순위가 높으면 top을 높은 순위로 바꾸기
            top = grade[i][1]
        else:
            # 순위가 낮으면 개수 감소
            n -= 1
    print(n)
